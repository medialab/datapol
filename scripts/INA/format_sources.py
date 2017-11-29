import csv
import json
import requests
from config import SERVER_URL

SEARCH_URL = '%s/twitter.dlweb/ppc/ws/search' % SERVER_URL

def get_first_tweet(screen_name):
    args = {
        'from': 0,
        'from_date': '',
        'hashtags': '',
        'index': 'twitter_search_lab02',
        'lang': '',
        'mentions': '',
        'query': 'user.screen_name:"%s"' % screen_name,
        'quote': '-1',
        'retweet': '-1',
        'size': 1,
        'sort_field': 'created_at',
        'sort_type': 'asc',
        'to_date': '',
        'users': ''
    }

    res = requests.post(SEARCH_URL, data=json.dumps(args))
    return res.json()

with open('./sources.jsonl', 'r') as sf, open('./sources.csv', 'w') as of:
    writer = csv.DictWriter(of, fieldnames=['id', 'account', 'description', 'tags'])
    writer.writeheader()

    for line in sf.readlines():
        if not line:
            continue

        data = json.loads(line)

        if data['type'] != 'timeline':
            continue

        row = {
            'id': '',
            'account': data['key'],
            'description': data['description'],
            'tags': '|'.join(data['extended_data']['tags']) if 'extended_data' in data else ''
        }

        if row['tags']:
            tweet = get_first_tweet(row['account'])

            if len(tweet['hits']):
                row['id'] = tweet['hits'][0]['_source']['user']['id']

        writer.writerow(row)
