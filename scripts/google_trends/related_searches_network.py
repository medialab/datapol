import networkx as nx
import json, sys, os

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit('USAGE : '+sys.argv[0]+' [sourceDir] [destQueryNet] [destEntityNet] [destBipartiteEnt]')#TODO
    G = nx.DiGraph()
    H = nx.Graph()
    Bipartite = nx.Graph()
    arbre = os.walk(sys.argv[1])
    bidict = {}
    for subrep in arbre:
        for filename in subrep[2]:
        # Related Query
            if filename.endswith('.json') and 'queries' in filename.split('§')[0]:
                entityfilename = 'entities§'+'§'.join(filename.split('§')[1:])
#                print(entityfilename)
#                print('Hell')
                query_list = []
#                entity_list = []
                with open(os.path.join(subrep[0], filename), 'r') as f:
                    related_query_json = json.load(f)

                    # Handle Bipartite generation
#                    if related_query_json['keyword'] not in bidict:
#                        bidict[related_query_json['keyword']] = []

                    # Add keyword node
                    keyword = related_query_json['keyword']
                    G.add_node(keyword)
                    Bipartite.add_node((keyword, 'q'), nodetype='q')
                    query_list.append((keyword, 'q'))

                    for related_query_list in related_query_json['default']['rankedList']:
                        for related_query_doc in related_query_list['rankedKeyword']:
                            # 1) Add the node to the graph
                            related_query = related_query_doc['query']
                            G.add_node(related_query)
                            Bipartite.add_node((related_query, 'q'), nodetype='q')
                            query_list.append((related_query, 'q'))
#                            bidict[related_query_json['keyword']].append((related_query_doc['query'], 'q'))
                            # 2) Add the edge
                            G.add_edge(keyword, related_query)
                            Bipartite.add_edge((keyword, 'q'), (related_query, 'q'))
        # Related Topics
#            elif filename.endswith('.json') and 'entities' in filename.split('§')[0] and os.stat(subrep[0]+filename).st_size != 0:
#                print('Yes')
                with open(os.path.join(subrep[0], entityfilename), 'r') as f:
                    related_topic_json = json.load(f)

                    # Handle Bipartite generation
#                    if related_topic_json['keyword'] not in bidict:
#                        bidict[related_topic_json['keyword']] = []

                    for related_topic_list in related_topic_json['default']['rankedList']:
                        for num_topic, related_topic_doc in enumerate(related_topic_list['rankedKeyword']):
                            # 1) Add the node to the graph
                            related_topic = related_topic_doc['topic']['title']
                            H.add_node(related_topic)
                            Bipartite.add_node((related_topic, 'e'), nodetype='e')
#                            bidict[related_topic_json['keyword']].append((related_topic_doc['topic']['title'], 'e'))
                            for i in range(num_topic + 1, len(related_topic_list['rankedKeyword'])):
                                other_topic = related_topic_list['rankedKeyword'][i]['topic']['title']
                                H.add_node(other_topic)
                                Bipartite.add_node((other_topic, 'e'), nodetype='e')
                                # 2) Add the edge
                                H.add_edge(related_topic, other_topic)
                                Bipartite.add_edge((related_topic, 'e'), (other_topic, 'e'))
                            for linked_query_tuple in query_list:
                                Bipartite.add_edge((related_topic, 'e'), linked_query_tuple)

#    for key, item in bidict.items():
#        key_tuple = (key, 'q')
#        Bipartite.add_node(key_tuple, nodetype='q')
#        for num_node, typed_node in enumerate(item):
#            Bipartite.add_node(typed_node, nodetype=typed_node[1])
#            for i in range(num_node + 1, len(item)):
#                Bipartite.add_node(item[i], nodetype=item[i][1])
#                Bipartite.add_edge(key_tuple, item[i])
 #               Bipartite.add_edge(typed_node, item[i])

    nx.write_gexf(G, sys.argv[2])
    nx.write_gexf(H, sys.argv[3])
    nx.write_gexf(Bipartite, sys.argv[4])