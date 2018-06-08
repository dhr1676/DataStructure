import sys


def Floyd(graph):
    _nodeNum = len(graph)
    _parentField = [[-1 for i in range(_nodeNum)] for j in range(_nodeNum)]

    for i in range(_nodeNum):
        for j in range(_nodeNum):
            if graph[i][j] != sys.maxsize:
                _parentField[i][j] = i

    for k in range(_nodeNum):
        for i in range(_nodeNum):
            for j in range(_nodeNum):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    _parentField[i][j] = _parentField[k][j]

    return graph, _parentField


if __name__ == '__main__':
    nodeNum = 4
    graph = [[0, 1, 1, 10],
             [1, 0, 10, 10],
             [1, 10, 0, 1],
             [10, 10, 1, 0]]

    shortestPath, parentField = Floyd(graph)

    for p in shortestPath:
        print(p)
    print("\n")

    for p in parentField:
        print(p)
