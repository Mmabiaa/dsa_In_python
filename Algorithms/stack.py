class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to hold stack elements

    def push(self, item):
        self.stack.append(item)  # Add an item to the top of the stack

    def pop(self):
        if not self.is_empty():  # Check if stack is not empty
            return self.stack.pop()  # Remove and return the top item
        return None  # Return None if stack is empty

    def peek(self):
        if not self.is_empty():  # Check if stack is not empty
            return self.stack[-1]  # Return the top item without removing it
        return None  # Return None if stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Return True if stack is empty, else False

    def size(self):
        return len(self.stack)  # Return the number of items in the stack
