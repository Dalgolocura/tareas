
import sys

class Edge :
    def __init__(self, u, v, weight) :
        self.u = u
        self.v = v
        self.weight = weight
    
class HeapNode :
    def __init__(self) :
        self.vertex = 0
        self.key = 0
    
class ResultSet :
    def __init__(self) :
        self.parent = 0
        self.weight = 0


class Heap():
    def __init__(self, capacity):
        self.capacity = capacity
        self.nodes = [None] * (capacity + 1)
        self.indexes = [0] * (capacity)
        self.nodes[0] = HeapNode()
        self.nodes[0].key = -sys.maxsize
        self.nodes[0].vertex = -1
        self.size = 0

    def newNode(self, n, dist):
        Node = [n, dist]
        return Node

    def swapNodes(self, a, b):
        n = self.nodes[a]
        self.nodes[a] = self.nodes[b]
        self.nodes[b] = n
    def heapSize(self) :
        return self.size

    def bubbleUp(self, pos) :
        parentIdx = int(pos / 2)
        currentIdx = pos
        while (currentIdx > 0 and 
               self.nodes[parentIdx].key > self.nodes[currentIdx].key) :
            currentNode = self.nodes[currentIdx]
            parentNode = self.nodes[parentIdx]
            self.indexes[currentNode.vertex] = parentIdx
            self.indexes[parentNode.vertex] = currentIdx
            self.swapNodes(currentIdx, parentIdx)
            currentIdx = parentIdx
            parentIdx = int(parentIdx / 2)

    def insert(self, x) :
        self.size += 1
        idx = self.size
        self.nodes[idx] = x
        self.indexes[x.vertex] = idx
        self.bubbleUp(idx)
    def isEmpty(self):
        return True if self.size == 0 else False

     # Standard function to extract minimum node from heap
    def extractMin(self) :
        min = self.nodes[1]
        lastNode = self.nodes[self.size]
        self.indexes[lastNode.vertex] = 1
        self.nodes[1] = lastNode
        self.nodes[self.size] = None
        self.sinkDown(1)
        self.size -= 1
        return min
    
    def sinkDown(self, k) :
        smallest = k
        leftChild = 2 * k
        rightChild = 2 * k + 1
        if (leftChild < self.heapSize() and 
            self.nodes[smallest].key > self.nodes[leftChild].key) :
            smallest = leftChild
        
        if (rightChild < self.heapSize() and 
            self.nodes[smallest].key > self.nodes[rightChild].key) :
            smallest = rightChild
        
        if (smallest != k) :
            smallestNode = self.nodes[smallest]
            kNode = self.nodes[k]
            self.indexes[smallestNode.vertex] = k
            self.indexes[kNode.vertex] = smallest
            self.swapNodes(k, smallest)
            self.sinkDown(smallest)

    def isHeap(self, n):
 
        if self.pos_graph[n] < self.size:
            return True
        return False
 
 
def printArr(parent, n):
    for i in range(1, n):
        print("% d - % d" % (parent[i], i))
    
    
class Graph:

    def __init__(self, no_vertices):
        self.vertices = []
        self.no_vertices = no_vertices
        i = 0
        while (i < self.no_vertices) :
            self.vertices.append([])
            i += 1
    def addEdge(self, v1, v2, e):
        self.vertices[v1].append(Edge(v1, v2, e))
        self.vertices[v2].append(Edge(v2, v1, e))

    def decreaseKey(self, minHeap, newKey, vertex) :
        index = minHeap.indexes[vertex]
        node = minHeap.nodes[index]
        node.key = newKey
        minHeap.bubbleUp(index)

    def Prims(self):
        inHeap = [False] * (self.no_vertices)
        resultSet = [None] * (self.no_vertices)
        key = [0] * (self.no_vertices)
        heapNodes = [None] * (self.no_vertices)
        i = 0 
    
        while (i < self.no_vertices) :
            heapNodes[i] = HeapNode()
            heapNodes[i].vertex = i
            heapNodes[i].key = sys.maxsize
            resultSet[i] = ResultSet()
            resultSet[i].parent = -1
            inHeap[i] = True
            key[i] = sys.maxsize
            i += 1
 
        heapNodes[0].key = 0
        minHeap = Heap(self.no_vertices)
        j = 0
        while (j < self.no_vertices) :
            minHeap.insert(heapNodes[j])
            j += 1
        
        i = 0
        while (minHeap.isEmpty() == False) :
            extractedNode = minHeap.extractMin()
            extractedVertex = extractedNode.vertex
            inHeap[extractedVertex] = False
            while (i < len(self.vertices[extractedVertex])) :
                edge = self.vertices[extractedVertex][i]
                if (inHeap[edge.v]) :
                    v = edge.v
                    w = edge.weight
                    if (key[v] > w) :
                        key[v] = w
                        self.decreaseKey(minHeap, w, v)
                        resultSet[v].parent = extractedVertex
                        resultSet[v].weight = w
                i += 1
            i = 0
        result = 0
        print("\n\n Minimum Spanning Tree ")
        node = 1
        while (node < self.no_vertices) :
            print(" Edge (", resultSet[node].parent ,"-", node ,
                  ")  weight : ", resultSet[node].weight)
            result += resultSet[node].weight
            node += 1
        print(" Total minimum weight : ", result)
    
    def printGraph(self) :
        print("\n Graph Adjacency List ", end = "")
        i = 0
        while (i < self.no_vertices) :
            print(" \n [", i ,"] :", end = "")
            j = 0
            while (j < len(self.vertices[i])) :
                print("  ", self.vertices[i][j].v, end = "")
                j += 1
            i += 1

graph = Graph(6)
graph.addEdge(0, 1, 6)
graph.addEdge(0, 2, 1)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 2, 5)
graph.addEdge(1, 4, 3)
graph.addEdge(2, 3, 5)
graph.addEdge(2, 4, 6)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 5, 2)
graph.addEdge(4, 5, 6)
graph.printGraph()
graph.Prims()

graph = Graph(7)
graph.addEdge(0, 1, 12)
graph.addEdge(0, 2, 7)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 2, 4)
graph.addEdge(1, 4, 7)
graph.addEdge(2, 3, 9)
graph.addEdge(2, 5, 4)
graph.addEdge(2, 4, 3)
graph.addEdge(3, 5, 7)
graph.addEdge(4, 5, 2)
graph.addEdge(4, 6, 2)
graph.addEdge(5, 6, 5)
graph.printGraph()
graph.Prims()