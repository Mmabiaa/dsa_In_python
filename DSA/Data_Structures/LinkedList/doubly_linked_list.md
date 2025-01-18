# Doubly Linked List

A **Doubly Linked List** is a type of linked list in which each node contains a reference to both the next and the previous node. This allows for traversal in both directions.

## Operations

### 1. Append
- Adds a new node at the end of the list.

### 2. Display
- Prints all elements in the list from head to tail.

### 3. Delete
- Removes a node with a specified value from the list.

### 4. Reverse
- Reverses the order of nodes in the list.

## Complexity Analysis

- **Time Complexity**:
  - Append: O(n) in worst case (if we need to traverse to the end).
  - Delete: O(n) in worst case (if we need to traverse to find the node).
  - Reverse: O(n) as we traverse through all nodes once.
  
- **Space Complexity**: O(1) as we only use a fixed amount of extra space.

## Example Usage

```
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display() # Output: 1 2 3
dll.delete(2)
dll.display() # Output: 1 3
dll.reverse()
dll.display() # Output: 3 1
```
