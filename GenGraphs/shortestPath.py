import networkx as nx
import numpy as np

n_vertices=8
G=nx.generators.geometric.random_geometric_graph(n_vertices, 0.8)

matrix=nx.adjacency_matrix(G)
matrix=np.array(matrix.todense(),dtype=int)

count=np.count_nonzero(matrix)
nums = np.random.randint(1,10, count)

matrix[np.where(matrix!=0)]=nums

a=np.random.randint(0,7)
b=np.random.randint(0,7)
print(matrix)

with open('SP.txt', 'wt') as f:
    f.write("%d %d\n"%(a,b))
    for row in range(0,n_vertices):
        for col in range(0,n_vertices):
            f.write("%d"%matrix[row,col])
            if col == n_vertices-1: f.write("\n")
            else: f.write(" ")
