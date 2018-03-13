#!/usr/bin/env python3
import csv
import json
import os
from datetime import datetime
from os.path import join

# Parameters
DATASET_PATH = './dataset'
OUTPUT_PATH = './'

# Helpers
def json_files_iter(path):
    for root, dirs, files in os.walk(DATASET_PATH):
        for filename in files:
            if not filename.endswith('.json'):
                continue

            with open(join(root, filename), 'r') as f:
                yield filename, f

def json_tweets_iter(file):
    for line in file.readlines():
        line = line.strip()

        if not line:
            continue

        yield json.loads(line)

# Converting dataset
for json_filename, json_file in json_files_iter(DATASET_PATH):
    print('Processing %s...' % json_filename)

    output_filename = '%s-tweets.csv' % json_filename.split('_')[0]

    with open(join(OUTPUT_PATH, output_filename), 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['source', 'time', 'tweet', 'targets'])
        writer.writeheader()

        for tweet in json_tweets_iter(json_file):
            row = {
                'source': '@' + tweet['user']['screen_name'],
                'time': datetime.fromtimestamp(int(tweet['timestamp_ms']) / 1000).strftime("%Y-%m-%dT%H:%M:%S"),
                'tweet': tweet['id_str']
            }

            entities = tweet['entities']
            targets = []

            for hashtag in entities['hashtags']:
                targets.append('#' + hashtag['text'])

            for mention in entities['user_mentions']:
                targets.append('@' + mention['screen_name'])

            row['targets'] = '|'.join(targets)

            writer.writerow(row)
