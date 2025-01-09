
---

### **7. Heap (Min-Heap and Max-Heap): Insert, Extract Min/Max, Peek, Delete, Heapify**

#### **Markdown File (`heap.md`)**
```markdown
# Heap Operations: Insert, Extract Min/Max, Peek, Delete, Heapify

### Introduction
A **Heap** is a special tree-based data structure that satisfies the heap property. A **Min-Heap** is a binary tree where the value of each parent node is less than or equal to its children, while a **Max-Heap** has a parent node greater than or equal to its children.

### Methods:
1. **Insert**: Adds a new element to the heap.
2. **Extract Min/Max**: Removes the minimum (or maximum) element from the heap.
3. **Peek**: Returns the root element of the heap without removing it.
4. **Delete**: Removes an element from the heap.
5. **Heapify**: Maintains the heap property by arranging the elements.

### Python Code:
```python
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        """Insert a new element into the heap."""
        heapq.heappush(self.heap, val)

    def extract_min(self):
        """Extract and return the minimum element."""
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        """Return the minimum element without removing it."""
        if self.heap:
            return self.heap[0]
        return None

    def delete(self, val):
        """Delete a specific element from the heap."""
        try:
            self.heap.remove(val)
            heapq.heapify(self.heap)
        except ValueError:
            pass

    def heapify(self):
        """Maintain the heap property."""
        heapq.heapify(self.heap)

# Example usage
min_heap = MinHeap()
min_heap.insert(20)
min_heap.insert(15)
min_heap.insert(30)
min_heap.insert(10)

print("Min-Heap Peek:", min_heap.peek())
print("Extract Min:", min_heap.extract_min())
min_heap.delete(15)
print("Min-Heap After Deletion:", min_heap.heap)
