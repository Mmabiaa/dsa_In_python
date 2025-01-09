
---

### **4. Queue: Enqueue, Dequeue, Peek, IsEmpty, Size**

#### **Markdown File (`queue.md`)**
```markdown
# Queue Operations: Enqueue, Dequeue, Peek, IsEmpty, and Size

### Introduction
A **Queue** is a linear data structure that follows the **First In First Out (FIFO)** principle. Elements are added at the **rear** and removed from the **front**.

### Methods:
1. **Enqueue**: Adds an item to the rear of the queue.
2. **Dequeue**: Removes the front item from the queue.
3. **Peek**: Returns the front item without removing it.
4. **IsEmpty**: Checks if the queue is empty.
5. **Size**: Returns the number of items in the queue.

### Python Code:
```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty"

    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Front item:", q.peek())
print("Size of queue:", q.size())
print("Dequeued item:", q.dequeue())
print("Queue is empty:", q.is_empty())
