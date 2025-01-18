# Disjoint Set (Union-Find)

The **Disjoint Set** or **Union-Find** is a data structure that keeps track of a partition of a set into disjoint subsets. It supports union and find operations efficiently.

## Operations

### Find
- Determines which subset a particular element belongs to; this can be used for checking if two elements are in the same subset.

### Union
- Merges two subsets into a single subset.

## Complexity Analysis

- **Time Complexity**:
   - Find: O(α(n)), where α is the inverse Ackermann function.
   - Union: O(α(n)).
  
- **Space Complexity**: O(n), where n is the number of elements in disjoint sets.

## Example Usage
```
ds = DisjointSet()
ds.union('A', 'B')
ds.union('B', 'C')
print(ds.find('A')) # Output: A (root of A's set)
print(ds.find('C')) # Output: A (C is connected to A through B)
