import csv
import json
import math
import datetime
import requests
from config import SERVER_URL

# Constants
START_DATE = datetime.date(2017, 1, 1)
END_DATE = datetime.date(2017, 7, 1)
SEARCH_URL = '%s/twitter.dlweb/ppc/ws/search' % SERVER_URL
BULK_SIZE = 1000

# Helpers
def get_tweets(url, skip=0):
    args = {
        'from': skip,
        'from_date': START_DATE.strftime('%d-%m-%Y'),
        'hashtags': '',
        'index': 'twitter_search_lab02',
        'lang': '',
        'mentions': '',
        'query': 'urls.expanded_url:"%s"' % url,
        'quote': '-1',
        'retweet': '-1',
        'size': BULK_SIZE,
        'sort_field': 'created_at',
        'sort_type': 'asc',
        'to_date': END_DATE.strftime('%d-%m-%Y'),
        'users': '',
        'date_start': int(START_DATE.timestamp() * 1000),
        'date_stop': int(END_DATE.timestamp() * 1000)
    }

    res = requests.post(SEARCH_URL, data=json.dumps(args))
    return res.json()

def extract_row(url, data):
    return {
        'account': data['user']['screen_name'],
        'url': url,
        'tweet': data['id'],
        'time': datetime.datetime.fromtimestamp(int(data['created_at']) / 1000).isoformat(),
        'retweeted': 'x' if data['retweeted'] else '',
        'quote': 'x' if data['quote'] else ''
    }

def rows_iter(url, data):
    for hit in data['hits']:
        yield extract_row(url, hit['_source'])

# Opening buffers
url_file = open('./toplinks.csv', 'r')
triplets_file = open('./triplets.csv', 'w')
triplets_fieldnames = [
    'account',
    'url',
    'tweet',
    'time',
    'retweeted',
    'quote'
]

url_reader = csv.DictReader(url_file)

writer = csv.DictWriter(triplets_file, fieldnames=triplets_fieldnames)
writer.writeheader()

# Iterating over the mined URLs
for i, url_doc in enumerate(url_reader):
    url = url_doc['URL']

    print('(%i) Processing & polling "%s"' % (i + 1, url))

    # Getting first page of results
    first_page = get_tweets(url)
    data = get_tweets(url)
    total_count = data['total_count']
    todo_count = max(0, total_count - BULK_SIZE)

    queries_nb = math.ceil(todo_count / BULK_SIZE)

    print('Need to fetch %i more tweets. (We estimated %i). This will require %i more queries.' % (
        todo_count,
        max(0, int(url_doc['Nb docs']) - 1000),
        queries_nb
    ))

    # Dumping first page
    for row in rows_iter(url, data):
        writer.writerow(row)

    # Processing the rest
    for j in range(1, queries_nb + 1):
        skip = j * BULK_SIZE
        print('  (%i) One more query...' % j)

        for row in rows_iter(url, get_tweets(url, skip=skip)):
            writer.writerow(row)

    print()

# Tearing down
url_file.close()
output_file.close()
