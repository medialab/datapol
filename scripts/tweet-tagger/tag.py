#!/usr/bin/env python3
import re
import csv
import pandas as pd
from urllib.parse import urlparse
from collections import defaultdict, Counter
from progressbar import ProgressBar
from subprocess import check_output

# PARAMETERS
# -----------------------------------------------------------------------------
# Edit variables below to tweak script behavior.
# -----------------------------------------------------------------------------

# Path to the tweets CSV file
TWEETS_PATH = './politoscope-sample.csv'

# Path to the categorised urls CSV file
URLS_PATH = './decodex.csv'

# Path to the output CSV file
OUTPUT_PATH = './tagged-politoscope-sample.csv'

# Name of the column containing the url
URL_COLUMN = 'attr_home'

# Name of the columns containing category information
CATEGORIES_COLUMNS = {
    'Id': 'decodex_id',
    'attr_home': 'decodex_source',
    'Fiabilité': 'decodex_fiability',
    'Catégorie': 'decodex_category',
    'Orientation contenu': 'decodex_orientation'
}

# Name of the column containing the list of a tweet's links
LINKS_COLUMN = 'url'

# Csv delimiter of the tweet's file
DELIMITER = ' '

# Name of the value given to untagged links in a category
UNTAGGED_VALUE = 'untagged'

# Max number of rows of CSV file to process, useful for debugging
LIMIT = None

# Should the script avoid to report tweets without links?
COMPACT = True

# Should the script filter untagged lines?
FILTER_UNTAGGED = False

# SCRIPT
# -----------------------------------------------------------------------------

URL_BLACK_LIST = frozenset([
    'http://instagram.com',
    'http://plus.google.com',
    'http://facebook.com',
    'http://dailymotion.com',
    'http://youtube.com',
    'http://twitter.com',
    'http://fr.wikipedia.org',
    'http://wikihow.com'
])

# Helper classes & functions

# Notes:
#   1) We will drop the scheme. It's not relevant for us right now.
#   2) Some urls are filtered for relevance (e.g. twitter.com)
#   3) www variations needs to be taken into account
#   4) We need to avoid the TLD
def url_to_lru(url):
    parsed = urlparse(url)
    loc = ''
    port = ''

    if ':' in parsed.netloc:
        loc, port = parsed.netloc.split(':')
    else:
        loc = parsed.netloc

    stems = [
        # 's:' + parsed.scheme,
        't:' + port
    ]

    stems += ['h:' + x for x in reversed(loc.split('.')[:-1])]
    stems += ['p:' + x for x in parsed.path.split('/')]
    stems += ['q:' + parsed.query, 'f:' + parsed.fragment]

    stems = [stem for stem in stems if len(stem) > 2]

    return stems

def generate_www_variation(lru):
    if 'h:www' in lru:
        return [stem for stem in lru if stem != 'h:www']
    else:
        if len([stem for stem in lru if stem.startswith('h:')]) > 1:
            return None

        if lru[0].startswith('t:'):
            return lru[:2] + ['h:www'] + lru[2:]
        else:
            return lru[:1] + ['h:www'] + lru[1:]


class LRUTrie(object):

    def __init__(self, index):
        self.index = index
        self.root = {}
        self.leaf = 1

    def add(self, url):
        lru = url_to_lru(url)
        node = self.root

        for stem in lru:
            if stem not in node:
                node[stem] = {}

            node = node[stem]

        node[self.leaf] = url

        # Handling variation
        variation = generate_www_variation(lru)

        if variation:

            node = self.root

            for stem in variation:
                if stem not in node:
                    node[stem] = {}

                node = node[stem]

            node[self.leaf] = url

    def longest(self, url):
        lru = url_to_lru(url) + [None]
        node = self.root

        last_leaf = None

        for stem in lru:

            if self.leaf in node:
                last_leaf = node[self.leaf]

            if stem not in node:
                break

            node = node[stem]

        if last_leaf is None:
            return

        return self.index[last_leaf]

# Constants
URLS = defaultdict(dict)

# 1) We need to read the url file to build our URLS index
print('Building URL categories index...')
df = pd.read_csv(URLS_PATH, engine='c', dtype=str, usecols=[URL_COLUMN] + list(CATEGORIES_COLUMNS.keys()))

for i, row in df.iterrows():

    for column in CATEGORIES_COLUMNS.keys():

        # Filtering some irrelevant urls
        if row[URL_COLUMN] in URL_BLACK_LIST:
            continue

        URLS[row[URL_COLUMN]][column] = row[column]

# 2) We need to build the LRU Trie
print('Building LRU Trie...')
trie = LRUTrie(URLS)

for url in URLS:
    trie.add(url)

# 3) Streaming & tagging the tweets file
print('Streaming & tagging tweets...')

SPLITTER = re.compile('\\s+')

lines = int(SPLITTER.split(check_output(['wc', '-l', TWEETS_PATH]).decode('utf-8'))[1]) - 1
bar = ProgressBar(max_value=LIMIT if LIMIT else lines)

stats = defaultdict(Counter)

with open(TWEETS_PATH, 'r') as tf, open(OUTPUT_PATH, 'w') as of:
    i = 0

    reader = csv.DictReader(tf, delimiter=DELIMITER)

    output_fieldnames = reader.fieldnames + list(CATEGORIES_COLUMNS.values())
    writer = csv.DictWriter(of, fieldnames=output_fieldnames, delimiter=DELIMITER)
    writer.writeheader()

    for row in bar(reader):
        i += 1

        if LINKS_COLUMN not in row or not row[LINKS_COLUMN]:

            if not COMPACT:
                writer.writerow(row)

            if LIMIT and i == LIMIT:
                break

            continue

        links = row[LINKS_COLUMN].split('|')
        links_data = (trie.longest(link) for link in links)

        # Filter untagged?
        if FILTER_UNTAGGED and all(d is None for d in links_data):
            continue

        links_data = [data if data else {} for data in links_data]

        categories = defaultdict(list)

        for data in links_data:
            for category in CATEGORIES_COLUMNS:
                value = data.get(category, UNTAGGED_VALUE)
                categories[category].append(value)
                stats[category][value] += 1

        for source_column, values in categories.items():
            row[CATEGORIES_COLUMNS[source_column]] = '|'.join(values)

        writer.writerow(dict(row))

        if LIMIT and i == LIMIT:
            break

print('\n\nStats:')

for column, values in stats.items():
    print('  Column: "%s"' % column)

    sorted_values = sorted(values.items(), key=lambda item: (item[1], item[0]), reverse=True)

    for value, count in sorted_values:
        print('    %s - %i' % (value, count))

print('')
