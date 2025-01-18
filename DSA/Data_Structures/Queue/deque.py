class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0) if not self.is_empty() else None

    def remove_rear(self):
        return self.items.pop() if not self.is_empty() else None

    def peek_front(self):
        return self.items[0] if not self.is_empty() else None

    def peek_rear(self):
        return self.items[-1] if not self.is_empty() else None

    def display(self):
        return list(self.items)

# Example usage
if __name__ == "__main__":
    deque = Deque()
    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_front(0)
    print("Deque:", deque.display())
    
    deque.remove_front()
    print("After removing front:", deque.display())
    
    deque.remove_rear()
    print("After removing rear:", deque.display())
