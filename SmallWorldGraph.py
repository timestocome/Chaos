

# http://github.com/timestocome

# Collective dynamics of 'small-world' networks
# http://worrydream.com/refs/Watts-CollectiveDynamicsOfSmallWorldNetworks.pdf

# Tutorial NetworkX
# https://networkx.github.io/documentation/networkx-1.9/tutorial/index.html


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



# create plots
fig = plt.figure(figsize=(8,8))

# create graph
G = nx.Graph()


# create nodes and add to graph
nodes = np.arange(0, 10)
for n in nodes: G.add_node(n)



# create nearest neighbor connections
edges = []
for i in range(len(nodes)):
    if i == len(nodes) - 1:
        edges.append((i, 0))
    else:
        edges.append((i, i+1))

# create connections to node one node away
for i in range(len(nodes)):
    if i == len(nodes) - 2:
        edges.append((i, 0))
    elif i == len(nodes) - 1:
        edges.append((i, 1)) 
    else:
        edges.append((i, i+2))

# add edges
G.add_edges_from(edges)


fig.add_subplot(311)
plt.title("Original Small World")
nx.draw(G)





# probability of changing an edge
# p == 0 returns standard small world graph
# p == 1 returns small world graph with each edge randomly changed
p = .1
edges1 = edges[:]

n_edges_to_change = int(len(edges1) * p)
r_edges = np.random.random_integers(0, len(edges1)-1, n_edges_to_change)

for r in r_edges:
    # change values from old to new in selected connections
    del edges1[r]

    new_edge_1 = np.random.randint(0, G.number_of_nodes())
    new_edge_2 = np.random.randint(0, G.number_of_nodes())

    edges1.append((new_edge_1, new_edge_2))


# create new graph
G1 = nx.Graph()
G1.add_nodes_from(nodes)
G1.add_edges_from(edges1)


fig.add_subplot(312)
plt.title('P = 10%')
nx.draw(G1)









p = .8
edges2 = edges[:]

n_edges_to_change = int(len(edges2) * p)
r_edges = np.random.random_integers(0, len(edges2)-1, n_edges_to_change)

edges2 = edges[:]
for r in r_edges:

    del edges2[r]

    new_edge_1 = np.random.randint(0, G.number_of_nodes())
    new_edge_2 = np.random.randint(0, G.number_of_nodes())

    edges2.append((new_edge_1, new_edge_2))


# create new graph
G2 = nx.Graph()
G2.add_nodes_from(nodes)
G2.add_edges_from(edges2)


fig.add_subplot(313)
plt.title('P = 80%')
nx.draw(G2)


plt.show()



#################
# stats
print('Info:')
print('-------------------------')
print("Small World")
print(nx.info(G))
print('Density %.2lf' % nx.density(G))

print('     ')
print("Small World 10% change")
print(nx.info(G1))
print('Density %.2lf' % nx.density(G1))

print('     ')
print("Small World 80% change")
print(nx.info(G2))
print('Density %.2lf' % nx.density(G2))

