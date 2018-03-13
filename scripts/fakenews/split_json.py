#!/usr/bin/env python3
import csv
import json

with open('./offshore.json', 'r') as f, open('./offshore.csv', 'w') as of:
    data = json.loads(f.read())
    writer = csv.DictWriter(of, fieldnames=['text', 'screen_name', 'user_id', 'tweet_id', 'retweet_count', 'created_at'])
    writer.writeheader()

    for hits in data['hits']['hits']:
        source = hits['_source']

        if 'retweeted_status' in source:
            continue

        writer.writerow({
            'text': source['tx'],
            'screen_name': source['usr']['snm'],
            'user_id': source['usr']['id'],
            'tweet_id': source['id_str'],
            'retweet_count': source['retweet_count'],
            'created_at': source['ca']
        })
