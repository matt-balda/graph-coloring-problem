import random
import itertools
import networkx as nx
import matplotlib.pyplot as plt

def is_valid_coloring(graph, coloring):
    for u, v in graph.edges():
        if coloring[u] == coloring[v]:
            return False
    return True

def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        neighbors = {coloring.get(neigh) for neigh in graph.neighbors(node)}
        coloring[node] = next(color for color in itertools.count() if color not in neighbors)
    return coloring

n_nodes = 50
G = nx.Graph()
G.add_nodes_from(range(n_nodes))

for i in range(n_nodes):
    for j in range(i+1, n_nodes):
        if random.random() < 0.1:
            G.add_edge(i, j)

coloring_result = greedy_coloring(G)
print('Coloring:', coloring_result)
print('Is valid coloring: ', is_valid_coloring(G, coloring_result))
print('K: ', len(set(coloring_result.values())))

color_map = [coloring_result[node] for node in G.nodes()]
nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
plt.show()