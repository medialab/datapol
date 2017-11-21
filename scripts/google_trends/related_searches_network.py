import networkx as nx
import json, sys, os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit('USAGE : '+sys.argv[0]+' [sourceDir] [destQueryNet] [destEntityNet] [destBipartiteEnt]')#TODO
    G = nx.DiGraph()
    H = nx.Graph()
    arbre = os.walk(sys.argv[1])
    for subrep in arbre:
        for filename in subrep[2]:
            if filename.endswith('.json') and 'queries' in filename.split('§')[0] and os.stat(subrep[0]+filename).st_size != 0:
#                print('Hell')
                with open(os.path.join(subrep[0], filename), 'r') as f:
                    related_topic_json = json.load(f)
                    # Add keyword node
                    G.add_node(related_topic_json['keyword'])
                    for related_topic_list in related_topic_json['default']['rankedList']:
                        for related_topic_doc in related_topic_list['rankedKeyword']:
                            # 1) Add the node to the graph
                            G.add_node(related_topic_doc['query'])
                            # 2) Add the edge
                            G.add_edge(related_topic_json['keyword'], related_topic_doc['query'])
            elif filename.endswith('.json') and 'entities' in filename.split('§')[0] and os.stat(subrep[0]+filename).st_size != 0:
#                print('Yes')
                with open(os.path.join(subrep[0], filename), 'r') as f:
                    related_topic_json = json.load(f)
                    # Add keyword node
                    #H.add_node(related_topic_json['keyword'])
                    for related_topic_list in related_topic_json['default']['rankedList']:
                        for num_topic, related_topic_doc in enumerate(related_topic_list['rankedKeyword']):
                            # 1) Add the node to the graph
                            H.add_node(related_topic_doc['topic']['title'])
                            for i in range(len(related_topic_list['rankedKeyword']) - (num_topic+1)):
                                H.add_node(related_topic_list['rankedKeyword'][i]['topic']['title'])
                                # 2) Add the edge
                                H.add_edge(related_topic_doc['topic']['title'], related_topic_list['rankedKeyword'][i]['topic']['title'])
    nx.write_gexf(G, sys.argv[2])
    nx.write_gexf(H, sys.argv[3])