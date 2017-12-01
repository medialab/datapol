#!/usr/bin/env python3
import csv
import json

SITES_INDEX = {}

with open('./decodex.json', 'r') as input_file, open('./decodex.csv', 'w') as output_file:
    data = json.loads(input_file.read())

    for site_id, meta in data['sites'].items():
        SITES_INDEX[int(site_id)] = {
            'id': site_id,
            'fiability': meta[0],
            'description': meta[1],
            'label': meta[2],
            'slug': meta[3]
        }

    writer = csv.DictWriter(output_file, fieldnames=['id', 'url', 'fiability', 'description', 'label', 'slug'])
    writer.writeheader()

    for url, site_id in data['urls'].items():
        site_data = SITES_INDEX[site_id]

        writer.writerow({
            'id': site_id,
            'url': url,
            'fiability': site_data['fiability'],
            'description': site_data['description'],
            'label': site_data['label'],
            'slug': site_data['slug']
        })
