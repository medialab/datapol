import csv
import json
import math
import datetime
import requests
from config import SERVER_URL

# Constants
START_DATE = datetime.datetime(2017, 1, 1)
END_DATE = datetime.datetime(2017, 7, 1)
SEARCH_URL = '%s/twitter.dlweb/ppc/ws/search' % SERVER_URL
BULK_SIZE = 1000
SKIP = 0

# Output formats
TRIPLERS_FIELDNAMES = [
    'account',
    'url',
    'tweet',
    'time',
    'retweeted',
    'quoted'
]

ACCOUNTS_FIELDNAMES = [
    'id',
    'screen_name',
    'name',
    'lang',
    'description',
    'created_at',
    'url',
    'location',
    'favourites_count',
    'friends_count',
    'listed_count',
    'followers_count',
    'statuses_count'
]

# State
ACCOUNTS = set()

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
        'quoted': 'x' if data['quoted'] else ''
    }

def extract_account(data):
    account = {}

    for prop in ACCOUNTS_FIELDNAMES:
        if 'created_at' in data and prop == 'created_at':
            account['created_at'] = datetime.datetime.fromtimestamp(int(data['created_at']) / 1000).isoformat()
        elif prop in data:
            account[prop] = data[prop]

    return account

def rows_iter(url, data):
    for hit in data['hits']:
        yield extract_account(hit['_source']['user']), extract_row(url, hit['_source'])

# Opening buffers
url_file = open('./toplinks.csv', 'r')
triplets_file = open('./triplets.csv', 'w')
accounts_file = open('./accounts.csv', 'w')

url_reader = csv.DictReader(url_file)

triplets_writer = csv.DictWriter(triplets_file, fieldnames=TRIPLERS_FIELDNAMES)
triplets_writer.writeheader()

accounts_writer = csv.DictWriter(accounts_file, fieldnames=ACCOUNTS_FIELDNAMES)
accounts_writer.writeheader()

# Iterating over the mined URLs
for i, url_doc in enumerate(url_reader):
    url = url_doc['URL']

    if i < SKIP:
        continue

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
    for account, row in rows_iter(url, data):
        triplets_writer.writerow(row)

        if account['screen_name'] not in ACCOUNTS:
            accounts_writer.writerow(account)
            ACCOUNTS.add(account['screen_name'])

    # Processing the rest
    for j in range(1, queries_nb + 1):
        skip = j * BULK_SIZE
        print('  (%i) One more query...' % j)

        for account, row in rows_iter(url, get_tweets(url, skip=skip)):
            triplets_writer.writerow(row)

            if account['screen_name'] not in ACCOUNTS:
                accounts_writer.writerow(account)
                ACCOUNTS.add(account['screen_name'])

    print()

# Tearing down
url_file.close()
triplets_file.close()
accounts_file.close()
