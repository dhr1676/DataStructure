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
        return None

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

    def __DFSRec(self, s, time):
        self.Vertexes[s].color = "Gray"
        self.Vertexes[s].time_in = time
        time += 1

        for v in self.Vertexes[s].edges.keys():
            if self.Vertexes[v].color == "White":
                self.Vertexes[v].parent = s
                time = self.__DFSRec(v, time)

        self.Vertexes[s].color = "Black"
        self.Vertexes[s].time_out = time
        time += 1

        return time

    def DFS(self, s):
        for i in range(self.size):
            self.Vertexes[i].color = "White"
            self.Vertexes[i].parent = -1
            self.Vertexes[i].time_in = -1
            self.Vertexes[i].time_out = -1

        self.__DFSRec(s, 0)
        return None

    def PrintShortestPath(self, u, v):
        if u == v:
            print(u, end="")
        elif self.Vertexes[v].parent == -1:
            print("unreachable")
        else:
            self.PrintShortestPath(u, self.Vertexes[v].parent)
            print(" -> %d" % v, end="")
        return None

    def __relax(self, u, v, v_weight):
        if self.Vertexes[u].distance + v_weight < self.Vertexes[v].distance:
            self.Vertexes[v].distance = self.Vertexes[u].distance + v_weight
            self.Vertexes[v].parent = u
        return None

    def Bellman_Ford(self, s):
        # Initialize all vertexes' distance and parent fields
        for i in range(self.size):
            self.Vertexes[i].distance = sys.maxsize
            self.Vertexes[i].parent = -1
        self.Vertexes[s].distance = 0

        # Bellman-Ford algorithm can find the shortest path in n-1 times
        for iteration in range(self.size - 1):
            # print("it is %d time" % iteration)
            for j in range(self.size):
                for v, v_weight in self.Vertexes[j].edges.items():
                    self.__relax(j, v, v_weight)
        # Detect negative circles
        for i in range(self.size):
            for v, v_weight in self.Vertexes[i].edges.items():
                if self.Vertexes[v].distance > self.Vertexes[i].distance + v_weight\
                        and self.Vertexes[i].distance != sys.maxsize:
                    # raise Exception("Negative edge")
                    print("Negative edge")

        return None

    def Dijkstra(self, s):

        return None


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

    # BFS and DFS test
    graph = Graph(7)
    graph.AddUndirectedEdge(0, 1)
    graph.AddUndirectedEdge(0, 2)
    graph.AddUndirectedEdge(1, 3)
    graph.AddUndirectedEdge(1, 4)
    graph.AddUndirectedEdge(2, 5)
    graph.AddUndirectedEdge(2, 6)
    graph.PrintGraph()

    # Print Breadth-first Search Tree
    graph.getBFT(0).PrintGraph()
    graph.PrintGraph()

    graph.DFS(0)
    graph.PrintGraph()

    # Bellman-Ford test
    g = Graph(10)
    g.AddUndirectedEdge(0, 1)
    g.AddUndirectedEdge(0, 2)
    g.AddUndirectedEdge(1, 4)
    g.AddUndirectedEdge(2, 3)
    g.AddUndirectedEdge(3, 4)
    g.AddUndirectedEdge(3, 6)
    g.AddUndirectedEdge(5, 6)
    g.AddUndirectedEdge(5, 8)
    g.AddUndirectedEdge(6, 7)
    g.AddUndirectedEdge(7, 9)
    g.AddUndirectedEdge(8, 9)
    g.Bellman_Ford(0)
    for t in range(10):
        print("\nShortest path from 0 to %d:\n" % t, end="")
        g.PrintShortestPath(0, t)
