from graph_model_demo import *


def printPath(path):
    """假设path是节点列表"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i + 1 != len(path):
            result = result + '->'
    return result


# 最短路径的深度优先搜索算法
def DFS(graph, start, end, path, shortest, toPoint=False):
    """假设 graph是无向图；
            start和end是节点；
            path和shortest是节点列表；
       返回graph中从start到end的最短路径 """
    path = path + [start]
    if toPoint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPoint)
                if newPath != None:
                    shortest = newPath
    return shortest



# 最短路径的广度优先搜索算法
def BFS(graph, start, end, toPoint=False):
    """假设graph是无向图；start和end是节点
       返回graph中从start到end的最短路径"""
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def shortestPath(graph, start, end, toPoint=False):
    """假设graph是无向图；start和end是节点
       返回graph中从start到end的最短路径。"""
    return DFS(graph, start, end, [], None, toPoint)


def testDFS():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp1 = shortestPath(g, nodes[0], nodes[5], toPoint=True)
    print('Shortest path found by DFS:', printPath(sp1))
    sp2 = BFS(g, nodes[0], nodes[5])
    print('Shortest path found by BFS:', printPath(sp2))


testDFS()
