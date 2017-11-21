import networkx as nx
import json, sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('USAGE : '+sys.argv[0]+' [...]')#TODO
    G = nx.DiGraph()
    #arbre = os.walk(sys.argv[1])
    #for subrep in arbre:
     #   for filename in subrep[2]:
      #      if filename.endswith('.json') and 'queries' in filename and os.stat(subrep[0]+filename).st_size != 0:
    with open(sys.argv[1], 'r') as f:
                    related_topic_json = json.load(f)
                    # Add keyword node
                    G.add_node(related_topic_json['keyword'])
                    for related_topic_list in related_topic_json['default']['rankedList']:
                        for related_topic_doc in related_topic_list['rankedKeyword']:
                            # 1) Add the node to the graph
                            G.add_node(related_topic_doc['query'])
                            # 2) Add the edge
                            G.add_edge(related_topic_json['keyword'], related_topic_doc['query'])
    nx.write_gexf(G, sys.argv[2])