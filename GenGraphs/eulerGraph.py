import networkx as nx
import numpy as np

flag=True

G=None
while flag:
    flag=False
    try:
        n_vertices=np.random.randint(6,10)
        degrees=[2,4,6,8]
        degree_sequence=None
        for i in range(n_vertices):
            degree_sequence=np.random.choice(degrees,n_vertices, replace=True)
        G=nx.random_degree_sequence_graph(degree_sequence)
    except (nx.NetworkXUnfeasible,  nx.NetworkXError):
        flag=True

matrix=nx.adjacency_matrix(G)
matrix=np.array(matrix.todense(),dtype=int)

print(matrix)

with open('euler.txt', 'wt') as f:
    for row in range(0,n_vertices):
        for col in range(0,n_vertices):
            f.write("%d"%matrix[row,col])
            if col == n_vertices-1: f.write("\n")
            else: f.write(" ")
