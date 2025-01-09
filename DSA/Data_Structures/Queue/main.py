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