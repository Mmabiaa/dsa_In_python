# Priority Queue

A **Priority Queue** is an abstract data type similar to a regular queue but with an added feature that allows elements with higher priority to be dequeued before those with lower priority.

## Operations

### 1. Put
- Adds an item to the queue with a specified priority.

### 2. Get
- Removes and returns the item with the highest priority.

### 3. Peek
- Returns the item with the highest priority without removing it.

## Complexity Analysis

- **Time Complexity**:
  - Put: O(log n), where n is the number of elements in the queue.
  - Get: O(log n).
  
- **Space Complexity**: O(n), where n is the number of elements in the queue.

## Example Usage
```
pq = PriorityQueue()
pq.put("task low", 3)
pq.put("task medium", 2)
pq.put("task high", 1)
while not pq.is_empty():
print(pq.get())
Output:
task high
task medium
task low
