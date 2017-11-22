import networkx as nx
import json, sys, os

if __name__ == '__main__':
    if len(sys.argv) < 5:
        sys.exit('USAGE : '+sys.argv[0]+' [sourceDir] [destQueryNet] [destEntityNet] [destBipartiteEnt]')
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
                query_list = []
                with open(os.path.join(subrep[0], filename), 'r') as f:
                    related_query_json = json.load(f)

                    # Add keyword node
                    keyword = related_query_json['keyword']
                    G.add_node(keyword)
                    Bipartite.add_node((keyword, 'q'), nodetype='q', label=keyword)
                    query_list.append((keyword, 'q'))

                    for related_query_list in related_query_json['default']['rankedList']:
                        for related_query_doc in related_query_list['rankedKeyword']:
                            related_query = related_query_doc['query']

                            # 1) Add the node to the query and bipartite graphs
                            G.add_node(related_query)
                            Bipartite.add_node((related_query, 'q'), nodetype='q', label=related_query)
                            # 1.1) Prepare
                            query_list.append((related_query, 'q'))

                            # 2) Add the edge
                            G.add_edge(keyword, related_query)
                            Bipartite.add_edge((keyword, 'q'), (related_query, 'q'))

                with open(os.path.join(subrep[0], entityfilename), 'r') as f:
                    related_topic_json = json.load(f)

                    for related_topic_list in related_topic_json['default']['rankedList']:

                        # 1) Add the nodes to the topic and bipartite graphs
                        for related_topic_doc in related_topic_list['rankedKeyword']:
                            related_topic = related_topic_doc['topic']['title']
                            H.add_node(related_topic)
                            Bipartite.add_node((related_topic, 'e'), nodetype='e', label=related_topic)

                        # 2) Add the edges
                        for num_topic, related_topic_doc in enumerate(related_topic_list['rankedKeyword']):
                            related_topic = related_topic_doc['topic']['title']

                            for i in range(num_topic + 1, len(related_topic_list['rankedKeyword'])):
                                other_topic = related_topic_list['rankedKeyword'][i]['topic']['title']
                                H.add_edge(related_topic, other_topic)
                                Bipartite.add_edge((related_topic, 'e'), (other_topic, 'e'))

                            # 2.1) Add bipartite graph topic-query edges
                            for linked_query_tuple in query_list:
                                Bipartite.add_edge((related_topic, 'e'), linked_query_tuple)

    nx.write_gexf(G, sys.argv[2])
    nx.write_gexf(H, sys.argv[3])
    nx.write_gexf(Bipartite, sys.argv[4])