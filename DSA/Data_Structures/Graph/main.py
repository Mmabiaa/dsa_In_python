from collections import deque
from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def dfs(self, vertex, visited=None):
        """Depth-First Search (DFS) algorithm."""
        if visited is None:
            visited = set()
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start_vertex):
        """Breadth-First Search (BFS) algorithm."""
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges from the graph."""
        if vertex in self.graph:
            self.graph.pop(vertex)
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.n = 0

    def add_vertex(self, vertex):
        """Add a vertex to the graph & increase its size."""
        self.graph[vertex] = []
        self.n += 1
    
    def remove_vertex(self, vertex):
        """Remove a vertex & its neighbors from the graph & decrease its size."""
        del self.graph[vertex]
        self.n -= 1

    def add_weighted_edge(self, vertex1:int, vertex2:int, weight:int):
        """Add a weighted edge between vertex1 and vertex2 & add a vertex if it's not in the graph yet"""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))

    def dfs(self, start_vertex):
        S = [start_vertex]
        visited = set()
        visited.add(start_vertex)
        while S:
            vertex = S.pop()
            print(vertex, end=" ")
            for neighbor, weight in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    S.append(neighbor)

    def dijkstra(self, start_vertex):
        """Dijkstra's algorithm."""
        distances = [float('inf')] * self.n
        distances[start_vertex] = 0
        min_heap = [(0, start_vertex)]
        while min_heap:
            curr_dist, vertex = heapq.heappop(min_heap)
            if curr_dist > distances[vertex]:
                continue
            for neighbor, weight in self.graph[vertex]:
                dist = curr_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(min_heap, (dist, neighbor))
        print(distances)
        return distances

# Example usage
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1, 2)
g.add_edge(1, 3)

print("DFS Traversal:", end=" ")
g.dfs(1)

print("\nBFS Traversal:", end=" ")
g.bfs(1)

g.remove_vertex(2)
print("\nGraph after removing vertex 2:", g.graph)

# Example usage - weighted graph
wg = WeightedGraph()

wg.add_weighted_edge(0, 1, 100)
wg.add_weighted_edge(0, 2, 10)
wg.add_weighted_edge(1, 3, 20)
wg.add_weighted_edge(2, 1, 1)
wg.add_weighted_edge(2, 3, 3)

print("\nWeighted graph:", wg.graph)
print("Size of the graph:", wg.n)

print("\nDFS Traversal from the vertex 0:", end=" ")
wg.dfs(0)

print("\nShortest distances from vertex 0 to the other nodes:")
wg.dijkstra(0)

wg.add_vertex(4)
print("\nWeighted graph after adding vertex 4:", wg.graph)
print("Size of the weighted graph after adding vertex 4:", wg.n)

wg.remove_vertex(4)
print("\nWeighted graph after removing vertex 4:", wg.graph)
print("Size of the weighted graph after removing vertex 4:", wg.n)
