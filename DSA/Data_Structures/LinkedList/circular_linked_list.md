# Circular Linked List

A **Circular Linked List** is a variation of a linked list where the last node points back to the first node, forming a circular structure.

## Operations

### 1. Append
- Adds a new node at the end of the list, ensuring that it points back to the head.

### 2. Display 
- Prints all elements in the circular linked list until it returns to the head.

## Complexity Analysis

- **Time Complexity**: 
  - Append: O(n) in worst case (if we need to traverse to find the end).
  
- **Space Complexity**: O(1) as we only use a fixed amount of extra space.

## Example Usage
```
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print(cll.display()) # Output: "1 -> 2 -> 3"
```
