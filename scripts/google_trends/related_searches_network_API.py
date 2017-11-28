import pprint
from apiclient.discovery import build

from config import *

def main():
  service = build('trends', 'v1beta',
                  developerKey=API_KEY,
                  discoveryServiceUrl=DISCOVERY_URL)

  # Single Graph Example, no restrictions
#  graph = service.getRisingQueries(term='macron', restrictions_geo='FR', restrictions_startDate='2017-01', restrictions_endDate='2017-06')
  graph = service.getGraph(terms=['osons causer', 'cyclohexane'], restrictions_geo='FR', restrictions_startDate='2017-01', restrictions_endDate='2017-06')
  response = graph.execute()
  pprint.pprint(response)


if __name__ == '__main__':
  main()
