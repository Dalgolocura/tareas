class Graph:
    def __init__(self):
        self.adjacencies = []
        self.vertices = []
        self.vertices_no = 0

    # Add a vertex to the set of vertices and the graph
    def add_vertex(self, v):
        if v in self.vertices:
            print("Vertex ", v, " already exists")
        else:
            self.vertices_no = self.vertices_no + 1
            self.vertices.append(v)
            if self.vertices_no > 1:
                for vertex in self.adjacencies:
                    vertex.append(0)
            temp = []
            for i in range(self.vertices_no):
                temp.append(0)
            self.adjacencies.append(temp)

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.vertices:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v1 is a valid vertex
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
        # Since this code is not restricted to a directed or
        # an undirected graph, an edge between v1 v2 does not
        # imply that an edge exists between v2 and v1
        else:
            index1 = self.vertices.index(v1)
            index2 = self.vertices.index(v2)
            self.adjacencies[index1][index2] = e

    # Print the graph
    def print(self):
        for i in range(self.vertices_no):
            for j in range(self.vertices_no):
                if self.adjacencies[i][j] != 0:
                    print(self.vertices[i], " -> ", self.vertices[j], \
                    " edge weight: ", self.adjacencies[i][j])

# Driver code
graph = Graph()
# Add vertices to the graph
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)
graph.add_edge(2, 3, 3)
graph.add_edge(3, 4, 4)
graph.add_edge(4, 1, 5)
graph.print()
print("Internal representation: ", graph)
