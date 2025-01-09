
---

### **2. Linked List: Insertion, Deletion, Search, Reverse, Traversal**

#### **Markdown File (`linked_list.md`)**
```markdown
# Linked List Operations: Insertion, Deletion, Search, Reverse, and Traversal

### Introduction
A **Linked List** is a linear data structure where each element (node) contains data and a reference (or pointer) to the next node. It does not have a fixed size and elements are not stored in contiguous memory locations.

### Methods:
1. **Insert**: Adds a node at the beginning of the list.
2. **Delete**: Removes the first occurrence of a node containing the specified value.
3. **Search**: Finds a node by its value.
4. **Reverse**: Reverses the entire linked list.
5. **Traverse**: Traverses and prints all the nodes in the list.

### Python Code:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first node containing the specified key."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        """Search for a node containing the specified key."""
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def reverse(self):
        """Reverse the linked list."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def traverse(self):
        """Traverse the list and return all nodes' data."""
        temp = self.head
        nodes = []
        while temp:
            nodes.append(temp.data)
            temp = temp.next
        return nodes

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
print("Linked List:", ll.traverse())

# Deleting node
ll.delete(20)
print("After Deletion:", ll.traverse())

# Searching
print("Search 10:", ll.search(10))
print("Search 100:", ll.search(100))

# Reversing the list
ll.reverse()
print("Reversed Linked List:", ll.traverse())