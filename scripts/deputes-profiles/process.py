#!/usr/bin/env python3
import pandas as pd
import csv
import math
from datetime import datetime
from progressbar import ProgressBar
from collections import defaultdict, namedtuple
from subprocess import check_output

# Constants
CHUNK_SIZE = 100
DEPUTES = set()
PROFILES = defaultdict(lambda: defaultdict(set))

# 1) We need to build the set of deputes' twitter accounts
df = pd.read_csv('./deputes.csv', engine='c', usecols=['twitter'])

for i, row in df.iterrows():
    DEPUTES.add(row['twitter'])

# 2) We need to iterate over the tweets to build our file
lines = int(str(check_output(['wc', '-l', './tweets.csv'])).split(' ')[1])
max_value = math.ceil(lines / CHUNK_SIZE)

bar = ProgressBar(max_value=max_value)

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

reader = pd.read_csv('./tweets.csv', engine='c', usecols=usecols,
                     iterator=True, chunksize=CHUNK_SIZE, dtype=dtype)

for chunk in bar(reader):
    for i, row in chunk.iterrows():

        # Some user don't have a description
        if pd.isnull(row['from_user_description']):
            continue

        # Filter account that are not deputes
        if row['from_user_name'] not in DEPUTES:
            continue

        description = row['from_user_description']
        date = datetime.fromtimestamp(row['time'])
        PROFILES[row['from_user_name']][description].add(date)

# 3) Dumping the results
with open('./profiles.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['depute', 'start', 'end', 'profile'])
    writer.writeheader()

    for depute, descriptions in PROFILES.items():
        points = []

        for description, dates in descriptions.items():
            for date in dates:
                points.append((date, description))

        points = sorted(points)

        current_start = None
        current_date = None
        current_description = None

        for date, description in points:
            if current_description != description:

                # Flush
                if current_description is not None:
                    writer.writerow({
                        'depute': depute,
                        'start': current_start,
                        'end': date,
                        'profile': current_description
                    })

                current_date = date
                current_start = date
                current_description = description

        # Sink
        if current_description is not None:
            writer.writerow({
                'depute': depute,
                'start': current_start,
                'end': current_date,
                'profile': current_description
            })
