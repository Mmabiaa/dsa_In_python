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