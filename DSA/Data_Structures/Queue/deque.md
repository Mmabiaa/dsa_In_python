# Deque (Double-Ended Queue)

A **Deque** is a linear data structure that allows insertion and deletion of elements from both ends.

## Operations

### 1. Add Front
- Inserts an element at the front of the deque.

### 2. Add Rear
- Inserts an element at the rear of the deque.

### 3. Remove Front
- Removes an element from the front of the deque.

### 4. Remove Rear
- Removes an element from the rear of the deque.

### 5. Peek Front
- Returns the front element without removing it.

### 6. Peek Rear
- Returns the rear element without removing it.

## Complexity Analysis

- **Time Complexity**:
  - Add/Remove from front: O(n) in worst case (due to list operations).
  - Add/Remove from rear: O(1).
  
- **Space Complexity**: O(n), where n is the number of elements in the deque.

## Example Usage

deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print(deque.display()) # Output: [0, 1, 2]
deque.remove_front()
print(deque.display()) # Output: [1, 2]
