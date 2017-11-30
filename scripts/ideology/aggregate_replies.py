#!/usr/bin/env python3
import os
import csv
import json
from os.path import join

# Parameters
INPUT_PATH = './tweets.csv'
TEXT_PATH = './text.csv'
REPLIES_FOLDER = './replies'
OUTPUT_PATH = './tweets-with-replies.csv'

# State
TWEETS = {}

# Pooling tweets
with open(INPUT_PATH, 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        tweet_id = row[0]
        TWEETS[tweet_id] = None


# Solving tweets text
with open(TEXT_PATH, 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['tweet_id'] not in TWEETS:
            continue

        TWEETS[row['tweet_id']] = {
            'text': row['tweet_text'],
            'created_at': row['created_at']
        }

# Sanity check
for tweet_id, data in TWEETS.items():
    if data is None:
        print('Error: no data for %s' % tweet_id)

# Outputting replies
with open(OUTPUT_PATH, 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['id', 'created_at', 'text', 'reply', 'reply_id', 'reply_created_at'])
    writer.writeheader()

    for tweet_id, tweet_data in TWEETS.items():

        with open(join(REPLIES_FOLDER, '%s_replies.json' % tweet_id)) as rf:
            replies = json.loads(rf.read())

            first = True

            for reply in replies:
                row = {
                    'id': tweet_id,
                    'created_at': tweet_data['created_at'],
                    'text': tweet_data['text'] if first else '',
                    'reply': reply['tx'],
                    'reply_id': reply['id_str'],
                    'reply_created_at': reply['ca']
                }

                writer.writerow(row)

                first = False
