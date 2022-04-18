class Graph:
    def __init__(self):
        self.vertices = {}
        self.no_vertices = 0

    # Add a vertex to the dictionary
    def add_vertex(self, v):
        if v in self.vertices:
            print("Vertex ", v, " already exists.")
        else:
            self.no_vertices = self.no_vertices + 1
            self.vertices[v] = []

    # Add an edge between vertex v1 and v2 with edge weight e
    def add_edge(self, v1, v2, e):
        # Check if vertex v1 is a valid vertex
        if v1 not in self.vertices:
            print("Vertex ", v1, " does not exist.")
        # Check if vertex v2 is a valid vertex
        elif v2 not in self.vertices:
            print("Vertex ", v2, " does not exist.")
        else:
            # Since this code is not restricted to a directed or
            # an undirected vertices, an edge between v1 v2 does not
            # imply that an edge exists between v2 and v1
            temp = [v2, e]
            self.vertices[v1].append(temp)

    # Print the graph
    def print(self):
        for vertex in self.vertices:
            for edges in self.vertices[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# driver code
graph = Graph()

# stores the number of vertices in the graph
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
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)
