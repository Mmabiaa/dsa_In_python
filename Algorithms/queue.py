class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to hold queue elements

    def enqueue(self, item):
        self.queue.append(item)  # Add an item to the end of the queue

    def dequeue(self):
        if not self.is_empty():  # Check if queue is not empty
            return self.queue.pop(0)  # Remove and return the front item
        return None  # Return None if queue is empty

    def front(self):
        if not self.is_empty():  # Check if queue is not empty
            return self.queue[0]  # Return the front item without removing it
        return None  # Return None if queue is empty

    def is_empty(self):
        return len(self.queue) == 0  # Return True if queue is empty, else False

    def size(self):
        return len(self.queue)  # Return the number of items in the queue
