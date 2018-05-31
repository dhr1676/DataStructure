import sys
import copy


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
        print("---------------------------------------\n")

    def getBFT(self, s):
        temp = Graph(self.size)

        for i in range(self.size):
            temp.Vertexes.append(Vertex())
            temp.Vertexes[i] = copy.deepcopy(self.Vertexes[i])

        for i in range(self.size):
            temp.Vertexes[i].color = "White"
            temp.Vertexes[i].distance = sys.maxsize
            temp.Vertexes[i].parent = -1

        temp.Vertexes[s].color = "Gray"
        temp.Vertexes[s].distance = 0

        queue = list()
        queue.append(s)

        while len(queue):
            u = queue.pop(0)
            # print("u is %d " % u)
            for v, weight in temp.Vertexes[u].edges.items():
                if temp.Vertexes[v].color == "White":
                    temp.Vertexes[v].color = "Gray"
                    temp.Vertexes[v].parent = u
                    temp.Vertexes[v].distance = temp.Vertexes[u].distance + 1
                    queue.append(v)
                    # print("v is %d " % v)
            temp.Vertexes[u].color = "Black"

        for i in range(self.size):
            temp.Vertexes[i].edges.clear()

        for i in range(self.size):
            if temp.Vertexes[i].parent >= 0:
                u = temp.Vertexes[i].parent
                temp.AddEdge(u, i, 1)

        return temp

    def __DFSVisit(self, u, time):
        return

    def __Relax(self, u, edge):
        return


if __name__ == '__main__':
    # graph = Graph(8)
    # graph.AddUndirectedEdge(0, 1)
    # graph.AddUndirectedEdge(0, 4)
    # graph.AddUndirectedEdge(1, 5)
    # graph.AddUndirectedEdge(2, 3)
    # graph.AddUndirectedEdge(2, 5)
    # graph.AddUndirectedEdge(2, 6)
    # graph.AddUndirectedEdge(3, 6)
    # graph.AddUndirectedEdge(3, 7)
    # graph.AddUndirectedEdge(5, 6)
    # graph.AddUndirectedEdge(6, 7)
    # graph.PrintGraph()
    #
    # graph.getBFT(1).PrintGraph()
    #
    # graph.PrintGraph()
    graph = Graph(7)
    graph.AddUndirectedEdge(0, 1)
    graph.AddUndirectedEdge(0, 2)
    graph.AddUndirectedEdge(1, 3)
    graph.AddUndirectedEdge(1, 4)
    graph.AddUndirectedEdge(2, 5)
    graph.AddUndirectedEdge(2, 6)
    graph.PrintGraph()

    graph.getBFT(0).PrintGraph()
    graph.PrintGraph()
