import os
import json
from os.path import join, isfile
from magic_scale import MAGIC_WORDS, find_precision_by_mean

# Helpers
def parse_json_file_name(path):
    _, keywords, _ = path.split('§')

    return tuple(keywords.split(' + '))

def create_json_file_name(keyword, precision):
    return (
        'timeseries§%s + %s§France.json'
    ) % (keyword, precision)

def json_files_iter(folder):
    for path in os.listdir(folder):
        full_path = join(folder, path)

        if not isfile(full_path) or \
           not path.endswith('.json') or \
           not path.startswith('timeseries'):
            continue

        yield full_path, parse_json_file_name(path)

# Script
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        raise Exception('Expecting a folder containing json files.')

    json_folder = sys.argv[1]

    KEYWORDS = set()

    for _, (keyword, _) in json_files_iter(json_folder):
        KEYWORDS.add(keyword)

    for keyword in KEYWORDS:
        flat_keyword_series = []
        flat_precision_series = []

        for precision_keyword in MAGIC_WORDS:
            path = join(json_folder, create_json_file_name(keyword, precision_keyword))
            keyword_series = []
            precision_series = []

            with open(path, 'r') as f:
                data = json.loads(f.read())['default']['timelineData']

                for item in data:
                    keyword_series.append(item['value'][0])
                    precision_series.append(item['value'][1])

            flat_keyword_series.append(keyword_series)
            flat_precision_series.append(precision_series)

        best_precision = find_precision_by_mean(flat_precision_series, flat_keyword_series)

        print('Best precision for "%s" is "%s"' % (keyword, best_precision))
