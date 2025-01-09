class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop the top item from the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

# Example usage
s = Stack()
s.push(10)
s.push(20)
print("Top item:", s.peek())
print("Size of stack:", s.size())
print("Popped item:", s.pop())
print("Stack is empty:", s.is_empty())