import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1] if not self.is_empty() else None

    def peek(self):
        return self.elements[0][1] if not self.is_empty() else None

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.put("task low", 3)
    pq.put("task medium", 2)
    pq.put("task high", 1)

    print("Tasks in order of priority:")
    while not pq.is_empty():
        print(pq.get())
