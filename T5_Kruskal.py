class Graph:
    def __init__(self, nVertices):
        self.adjacencies = []
        self.vertices = {}
        self.vertices_no = 0
        for i in range(nVertices):
            self.add_vertex(i)

    def add_vertex(self, v):
        if self.vertices.get(v) is not None:
            print("Vertex ", v, " already exists")
        else:
            self.vertices[v] = self.vertices_no
            self.vertices_no = self.vertices_no + 1
            if self.vertices_no > 1:
                for vertex in self.adjacencies:
                    vertex.append(-1)
            temp = []
            for i in range(self.vertices_no):
                temp.append(-1)
            self.adjacencies.append(temp)

    def add_edge(self, v1, v2, e):
        if self.vertices.get(v1-1) is None:
            print("Vertex ", v1, " does not exist.")
        elif self.vertices.get(v2-1) is None:
            print("Vertex ", v2, " does not exist.")
        else:
            index1 = self.vertices.get(v1-1)
            index2 = self.vertices.get(v2-1)
            self.adjacencies[index1][index2] = e
            self.adjacencies[index2][index1] = e

    def print(self):
        total_weight = 0
        for i in range(self.vertices_no):
            for j in range(i, self.vertices_no):
                if self.adjacencies[i][j] != -1:
                    total_weight += self.adjacencies[i][j]
                    print(i+1, " - ", j+1,
                          " edge weight: ", self.adjacencies[i][j])
        print("Total weight: ", total_weight)

    def checkCycle(self, v1, v2):

        checked = {}

        queue = []

        for i in range(self.vertices_no):
            if self.adjacencies[v1][i] != -1:
                queue.append(i)

        while len(queue) > 0:
            v = queue.pop(0)
            if v == v2:
                return True

            for i in range(self.vertices_no):
                if self.adjacencies[v][i] != -1 and i not in queue and checked.get(i) is None:
                    queue.append(i)
                    checked[i] = True

        return False

    def kruskal(self):
        resul = Graph(self.vertices_no)
        # edges = (weight, v1, v2)
        edges = []
        nEdges = 0

        for i in range(self.vertices_no):
            for j in range(i, self.vertices_no):
                if self.adjacencies[i][j] != -1:
                    edges.append([self.adjacencies[i][j], i, j])

        edges = sorted(edges, key=lambda x: x[0], reverse=True)
        # print(edges)

        while nEdges < self.vertices_no - 1:
            weight, v1, v2 = edges.pop()
            # print(v1,v2, weight,resul.checkCycle(v1, v2))
            if resul.checkCycle(v1, v2) is False:
                resul.add_edge(v1+1, v2+1, weight)
                # print(v1 + 1, "-", v2 + 1, "-", weight)
                nEdges = nEdges + 1

        return resul


graph = Graph(6)

graph.add_edge(1, 2, 6)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 5, 3)
graph.add_edge(4, 3, 5)
graph.add_edge(4, 6, 2)
graph.add_edge(3, 5, 6)
graph.add_edge(3, 6, 4)
graph.add_edge(5, 6, 6)

graph.print()
# print(graph.adjacencies, graph.vertices)
graph.kruskal().print()

print("-"*50)

graph = Graph(7)
graph.add_edge(1, 2, 12)
graph.add_edge(1, 3, 7)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 3, 4)
graph.add_edge(2, 5, 7)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 6, 4)
graph.add_edge(3, 5, 3)
graph.add_edge(4, 6, 7)
graph.add_edge(5, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(6, 7, 5)

graph.print()
# print(graph.adjacencies, graph.vertices)
graph.kruskal().print()
