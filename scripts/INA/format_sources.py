import csv
import json

with open('./sources.jsonl', 'r') as sf, open('./sources.csv', 'w') as of:
    writer = csv.DictWriter(of, fieldnames=['account', 'description', 'tags'])
    writer.writeheader()

    for line in sf.readlines():
        if not line:
            continue

        data = json.loads(line)

        if data['type'] != 'timeline':
            continue

        writer.writerow({
            'account': data['key'],
            'description': data['description'],
            'tags': '|'.join(data['extended_data']['tags']) if 'extended_data' in data else ''
        })
