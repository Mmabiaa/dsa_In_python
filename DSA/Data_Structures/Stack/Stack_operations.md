
---

### **3. Stack: Push, Pop, Peek, IsEmpty, Size**

#### **Markdown File (`stack.md`)**
```markdown
# Stack Operations: Push, Pop, Peek, IsEmpty, and Size

### Introduction
A **Stack** is a linear data structure that follows the **Last In First Out (LIFO)** principle. Elements can only be added or removed from one end, called the **top**.

### Methods:
1. **Push**: Adds an item to the top of the stack.
2. **Pop**: Removes the top item from the stack.
3. **Peek**: Returns the top item without removing it.
4. **IsEmpty**: Checks if the stack is empty.
5. **Size**: Returns the number of items in the stack.

### Python Code:
```python
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
