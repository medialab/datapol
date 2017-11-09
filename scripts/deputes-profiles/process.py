#!/usr/bin/env python3
import pandas as pd
import csv
from datetime import datetime
from progressbar import ProgressBar
from collections import defaultdict, namedtuple

MIN = datetime.min
MAX = datetime.max

# Constants
DEPUTES = set()
PROFILES = defaultdict(lambda: defaultdict(lambda: {'start': MAX, 'end': MIN}))

# 1) We need to build the set of deputes' twitter accounts
df = pd.read_csv('./deputes.csv', engine='c', usecols=['twitter'])

for i, row in df.iterrows():
    DEPUTES.add(row['twitter'])

# 2) We need to iterate over the tweets to build our file
bar = ProgressBar()

usecols = [
    'time',
    'from_user_name',
    'from_user_description'
]

dtype = {
    'time': int,
    'from_user_name': str,
    'from_user_description': str
}

reader = pd.read_csv('./tweets.csv', engine='c', usecols=usecols, nrows=1000,
                     iterator=True, chunksize=10, dtype=dtype)

for chunk in bar(reader):
    for i, row in chunk.iterrows():

        # Some user don't have a description
        if pd.isnull(row['from_user_description']):
            continue

        # Filter account that are not deputes
        if row['from_user_name'] not in DEPUTES:
            continue

        related_range = PROFILES[row['from_user_name']][row['from_user_description']]
        new_date = datetime.fromtimestamp(row['time'])

        if new_date < related_range['start']:
            related_range['start'] = new_date
        if new_date > related_range['end']:
            related_range['end'] = new_date

# 3) Dumping the results
with open('./profiles.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['depute', 'start', 'end', 'profile'])
    writer.writeheader()

    for depute, descriptions in PROFILES.items():
        tuples = ((related_range['start'], description) for description, related_range in descriptions.items())

        for _, description in sorted(tuples):
            related_range = descriptions[description]

            writer.writerow({
                'depute': depute,
                'start': related_range['start'].isoformat(),
                'end': related_range['end'].isoformat(),
                'profile': description
            })
