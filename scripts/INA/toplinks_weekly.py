import requests, json, datetime, sys
from config import SERVER_URL


def dowload_from_api(args):
    print(json.dumps(args, indent=1))
    url = "%s/twitter.dlweb/ppc/ws/dashboard" % SERVER_URL
    res = requests.post(url, data=json.dumps(args))
    return res.json()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('USAGE : '+sys.argv[0]+' [destJSONtoplinksFilename]')
    args = {"query":"","from_date":"","to_date":"","hashtags":"","mentions":"","users":"","lang":"","retweet":"-1","quote":"-1","index":"twitter_search_lab02"}
    start_date = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 7, 1)
    increment = datetime.timedelta(days=7)
    all_top_links = []
    while start_date < end_date:
        next_date = start_date + increment
        start_date_string = start_date.strftime('%d-%m-%Y')
        next_date_string = next_date.strftime('%d-%m-%Y')

        args["dashboard_type"]="urls"
        args['from_date'] = start_date_string
        args['to_date'] = next_date_string

        result_user = dowload_from_api(args)
        all_top_links.append({'date':start_date_string, 'list':result_user})
#        print(json.dumps(result_user, indent=4))
        start_date = next_date
    with open(sys.argv[1], 'w') as f:
        json.dump(all_top_links, f, indent=4)
