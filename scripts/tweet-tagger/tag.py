#!/usr/bin/env python3
import csv
import pandas as pd
from urllib.parse import urlparse
from collections import defaultdict
from progressbar import ProgressBar
from subprocess import check_output

# PARAMETERS
# -----------------------------------------------------------------------------
# Edit variables below to tweak script behavior.
# -----------------------------------------------------------------------------
TWEETS_PATH = './tweets.csv'
URLS_PATH = './decodex.csv'
OUTPUT_PATH = './tagged-tweets.csv'
URL_COLUMN = 'attr_home'
CATEGORIES_COLUMNS = {
    'Fiabilité et orientation': 'fiability'
}
LINKS_COLUMN = 'links'
UNTAGGED_VALUE = 'untagged'

# SCRIPT
# -----------------------------------------------------------------------------

# Helper classes & functions
def url_to_lru(url):
    parsed = urlparse(url)
    loc = ''
    port = ''

    if ':' in parsed.netloc:
        loc, port = parsed.netloc.split(':')
    else:
        loc = parsed.netloc

    stems = [
        's:' + parsed.scheme,
        't:' + port
    ]

    stems += ['h:' + x for x in reversed(loc.split('.'))]
    stems += ['p:' + x for x in parsed.path.split('/')]
    stems += ['q:' + parsed.query, 'f:' + parsed.fragment]

    stems = [stem for stem in stems if len(stem) > 2]

    return stems

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
df = pd.read_csv(URLS_PATH, engine='c', usecols=[URL_COLUMN] + list(CATEGORIES_COLUMNS.keys()))

for i, row in df.iterrows():

    for column in CATEGORIES_COLUMNS.keys():
        URLS[row[URL_COLUMN]][column] = row[column]

# 2) We need to build the LRU Trie
print('Building LRU Trie...')
trie = LRUTrie(URLS)

for url in URLS:
    trie.add(url)

# 3) Streaming & tagging the tweets file
print('Streaming & tagging tweets...')
lines = int(str(check_output(['wc', '-l', TWEETS_PATH])).split(' ')[1]) - 1
bar = ProgressBar(max_value=lines)

with open(TWEETS_PATH, 'r') as tf, open(OUTPUT_PATH, 'w') as of:
    reader = csv.DictReader(tf)

    output_fieldnames = reader.fieldnames + list(CATEGORIES_COLUMNS.values())
    writer = csv.DictWriter(of, fieldnames=output_fieldnames)
    writer.writeheader()

    for row in bar(reader):

        if 'links' not in row or not row['links']:
            writer.writerow(row)
            continue

        links = row['links'].split('|')
        links_data = (trie.longest(link) for link in links)
        links_data = [data if data else {} for data in links_data]

        categories = defaultdict(list)

        for data in links_data:
            for category in CATEGORIES_COLUMNS:
                categories[category].append(data.get(category, UNTAGGED_VALUE))

        for source_column, values in categories.items():
            row[CATEGORIES_COLUMNS[source_column]] = '|'.join(values)

        writer.writerow(dict(row))
