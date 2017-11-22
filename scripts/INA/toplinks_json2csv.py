import sys, json, csv

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('USAGE : '+sys.argv[0]+' [srcJSON] [destCSVtoplinksFilename]')
    with open(sys.argv[1], 'r') as f:
        toplink_json = json.load(f)
        url_d = {}
        for week in toplink_json:
            for toplink in week['list']:
                if toplink['key'] not in ['missing', 'others']:
                    if toplink['key'] in url_d:
                        url_d[toplink['key']] += toplink['doc_count']
                    else:
                        url_d[toplink['key']] = toplink['doc_count']

    with open(sys.argv[2], 'w') as f:
        destCSV = csv.writer(f)
        destCSV.writerow(['URL', 'Nb docs'])
        for key, item in url_d.items():
            destCSV.writerow([key, item])