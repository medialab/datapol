#!/usr/bin/env python3
import csv
from os.path import join

PERIODS = [
    '2012-2017',
    '2017-2022'
]

DATASET_PATH = './dataset'
OUTPUT_PATH = './'

HEADERS_TO_ADD = [
    'twitter_tweets',
    'twitter_followers',
    'twitter_following',
    'twitter_listed',
    'twitter_favourites',
    'twitter_verified',
    'twitter_protected',
    'twitter_id',
    'twitter_name',
    'twitter_description',
    'twitter_created_at',
    'sites_web',
    'url_institution',
    'slug',
    'url_nosdeputes_api'
]

INDEX = {}

for period in PERIODS:
    source_filename = 'nosdeputes_%s.csv' % period
    supplementary_filename = 'deputes_%s.csv' % period
    output_filename = 'deputes_%s_with_full_data.csv' % period

    with open(join(DATASET_PATH, source_filename), 'r') as source_file, \
         open(join(DATASET_PATH, supplementary_filename), 'r') as supplementary_file, \
         open(join(OUTPUT_PATH, output_filename), 'w') as output_file:

        source_reader = csv.DictReader(source_file, delimiter=';')
        supplementary_reader = csv.DictReader(supplementary_file)

        ouput_fieldnames = source_reader.fieldnames + HEADERS_TO_ADD
        output_writer = csv.DictWriter(output_file, fieldnames=ouput_fieldnames)

        output_writer.writeheader()

        for row in supplementary_reader:

            if 'twitter' in row:
                INDEX[row['twitter']] = row

        for row in source_reader:

            if 'twitter' not in row or row['twitter'] not in INDEX:
                continue

            supplementary_row = INDEX[row['twitter']]

            for header in HEADERS_TO_ADD:
                if header in supplementary_row:
                    row[header] = supplementary_row[header]

            output_writer.writerow(row)
