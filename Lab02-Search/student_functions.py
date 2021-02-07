import numpy as np

def convertToDict(input):
    newMatrix = {}
    flag = 0
    for i in input:
        newMatrix[flag] = list()
        temp = 0
        for j in i:
            if int(j) > 0:
                newMatrix[flag].append(temp)
                temp = temp + 1
            else:
                temp = temp + 1
        flag = flag + 1
    return newMatrix

def convertToUscDict(input):
    newMatrix = {}
    flag = 0
    for i in input:
        newMatrix[flag] = list()
        temp = 0
        for j in i:
            relateNode = {}
            if int(j) > 0:
                relateNode[temp] = [int(j), flag]
                newMatrix[flag].append(relateNode)
                temp = temp + 1
            else:
                temp = temp + 1
        flag = flag + 1
    return newMatrix

def DFS(matrix, start, end):
    """
    BFS algorithm:
    Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes, each key is a visited node,
        each value is the adjacent node visited before it.
    path: list
        Founded path
    """
    # TODO: 
   
   
    path=[]
    visited={}
    newMatrix = convertToDict(matrix)
    key = start
    path.append(key)
    while key != end:
        tempPath=[]
        visited[key] = newMatrix[key]
        print(visited[key])
        for i in visited[key]:
            tempPath.append(i)
        print(tempPath)
        for i in tempPath:
            if i in visited.keys():
                continue
            key = i
        path.append(key)
        print(path)
    print(path)
    print(visited)
    
    return visited, path

def BFS(matrix, start, end):
    """
    DFS algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited 
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """

    # TODO: 
    
    path=[]
    visited={}
    newMatrix = convertToDict(matrix)
    key = start
    path.append(key)
    while end not in path:
        tempPath=[]
        visited[key] = newMatrix[key]
        for i in visited[key]:
            tempPath.append(i)
        if end in tempPath:
            path.append(end)
        else:
            key = tempPath[0]
            path.append(key)
    print(path)
    print(visited)
   
    return visited, path


def UCS(matrix, start, end):
    """
    Uniform Cost Search algorithm
     Parameters:visited
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    # fullPath=[]
    # visited={}
    # newMatrix = convertToUscDict(matrix)
    # print(newMatrix)

    # key = start
    # fullPath.append(key)
    # # listCostKey = newMatrix.keys()
    # minValue = None
    # tempVisited = {}
    # while end not in fullPath:
    #     tempKeyVisited = tempVisited.keys()
    #     for i in newMatrix[key]:
    #         costKey = i.keys()
    #         costKey = list(costKey)
    #         if costKey[0] not in tempKeyVisited and costKey[0] != start:
    #             tempVisited[costKey[0]] = i[costKey[0]]
    #     costKey = tempVisited.keys()
    #     costKey = list(costKey)
    #     key = costKey[0]
    #     for j in tempVisited:
    #         if minValue == None:
    #             minValue = tempVisited[costKey[0]][0]
    #         if tempVisited[j][0] < minValue and j not in path:
    #             minValue = tempVisited[j][0]
    #             key = j
    #     # print(key)
    #     visited[key] = tempVisited[key]
    #     tempVisited.pop(key)
    #     # print(visited)
    #     fullPath.append(key)
    # # fullPath.reverse()
    # path.append(end)
    # fullKey = end
    # while start not in path:
    #     path.append(visited[fullKey][1])
    #     fullKey = visited[fullKey][1]
    # path.reverse()
    # print(visited, path)
    return visited, path


def GBFS(matrix, start, end):
    """
    Greedy Best First Search algorithm
     Parameters:
    ---------------------------
    matrix: np array 
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
   
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

def Astar(matrix, start, end, pos):
    """
    A* Search algorithm
     Parameters:
    ---------------------------
    matrix: np array UCS
        The graph's adjacency matrix
    start: integer 
        start node
    end: integer
        ending node
    pos: dictionary. keys are nodes, values are positions
        positions of graph nodes
    Returns
    ---------------------
    visited
        The dictionary contains visited nodes: each key is a visited node, 
        each value is the key's adjacent node which is visited before key.
    path: list
        Founded path
    """
    # TODO: 
    path=[]
    visited={}
    return visited, path

