
---

### **8. Graph: Add Vertex, Add Edge, DFS, BFS, Remove Vertex**

#### **Markdown File (`graph.md`)**
```markdown
# Graph Operations: Add Vertex, Add Edge, DFS, BFS, and Remove Vertex

### Introduction
A **Graph** is a collection of nodes (vertices) and edges (connections between nodes). Graphs can be either **directed** or **undirected** and can represent many real-world problems.

### Methods:
1. **Add Vertex**: Adds a new vertex to the graph.
2. **Add Edge**: Adds an edge between two vertices.
3. **DFS**: Performs a Depth-First Search on the graph.
4. **BFS**: Performs a Breadth-First Search on the graph.
5. **Remove Vertex**: Removes a vertex from the graph.

### Python Code:
```python
from collections import deque

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
