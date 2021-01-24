import networkx as nx
import numpy as np

G=nx.generators.community.connected_caveman_graph(3, 4)
print(G)
matrix=nx.adjacency_matrix(G)
matrix=np.array(matrix.todense(),dtype=int)

upper=np.triu(matrix)

count=np.count_nonzero(upper)
nums = np.random.randint(1,10, count)

upper[np.where(upper!=0)] = nums
matrix=(upper+upper.T)
print(matrix)

np.savetxt('MST.txt', matrix, fmt='%d', delimiter=' ')