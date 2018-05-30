import sys


class Edge(object):
    def __init__(self, v=None, weight=1):
        self.v = v
        self.weight = weight


class Vertex(object):
    def __init__(self):
        self.color = ""
        self.parent = -1
        self.distance = sys.maxsize
        self.time_in = -1
        self.time_out = -1
        self.it = {}
        self.edges = {}


class Graph(object):
    # Color = {"White": 0, "Gray": 1, "Black": 2}

    def __init__(self, size):
        self.size = size
        self.Vertexes = []
        for i in range(size):
            self.Vertexes.append(Vertex())
            self.Vertexes[i].color = "White"
            self.Vertexes[i].parent = -1
            self.Vertexes[i].distance = sys.maxsize
            self.Vertexes[i].time_in = -1
            self.Vertexes[i].time_out = -1
            self.Vertexes[i].edges = {}

    def AddEdge(self, u, v, weight):
        self.Vertexes[u].edges[v] = weight
        return None

    def AddUndirectedEdge(self, u, v, weight=1):
        self.AddEdge(u, v, weight)
        self.AddEdge(v, u, weight)
        return None

    def PrintGraph(self):
        print("--------Printing out the Graph:--------")
        for i in range(self.size):
            print("Vertex %d : " % i, end="")
            if self.Vertexes[i].parent >= 0:
                print(", parent = %d " % self.Vertexes[i].parent, end="")
            if self.Vertexes[i].distance < sys.maxsize:
                print(", distance = %d " % self.Vertexes[i].distance, end="")
            if self.Vertexes[i].time_in >= 0:
                print(", time_in = %d " % self.Vertexes[i].time_in, end="")
            if self.Vertexes[i].time_out >= 0:
                print(", time_out = %d " % self.Vertexes[i].time_out, end="")

            print(", edges={", end="")
            for k, v in self.Vertexes[i].edges.items():
                print("%d -> %d " % (i, k), end="")
            print("}")
        print("---------------------------------------")

    def __DFSVisit(self, u, time):
        return

    def __Relax(self, u, edge):
        return


if __name__ == '__main__':
    graph = Graph(4)
    graph.AddUndirectedEdge(0, 1)
    graph.AddUndirectedEdge(0, 3)
    graph.AddUndirectedEdge(1, 2)
    graph.AddUndirectedEdge(2, 3)
    graph.PrintGraph()
