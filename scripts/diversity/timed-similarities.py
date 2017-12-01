#!/usr/bin/env python3
import csv
import networkx as nx
from statistics import pvariance

GRAPH = nx.Graph()

# Reading CSV data
with open('./similarities.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        GRAPH.add_edge(row['Comm1'], row['Comm2'])
        edge = GRAPH.edges[row['Comm1'], row['Comm2']]

        if 'series' not in edge:
            edge['series'] = []

        edge['series'].append((int(row['Time']), float(row['Distance'])))

print(len(GRAPH), 'nodes')

# Sorting by variance
data = GRAPH.edges.data('series')
sorted_data = sorted(data, key=lambda x: pvariance([i[1] for i in x[2]]), reverse=True)

# Output
with open('./series.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['pair', 'source', 'target', 'time', 'similarity'])
    writer.writeheader()

    for source, target, series in sorted_data:
        for time, similarity in series:
            writer.writerow({
                'pair': '%s - %s' % (source, target),
                'source': source,
                'target': target,
                'time': time,
                'similarity': max(0, similarity - 0.5)
            })
