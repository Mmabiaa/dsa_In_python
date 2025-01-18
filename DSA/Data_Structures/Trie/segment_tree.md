
# Segment Tree

A **Segment Tree** is a binary tree used for storing intervals or segments. It allows querying which segments overlap with a given point efficiently and can also be used for range queries like sum or minimum.

## Operations

### Build
- Constructs the segment tree from a given array.

### Update
- Updates a specific index in the original array and reflects this change in the segment tree.

### Query
- Returns the sum (or other aggregate function) of a given range [left, right).

## Complexity Analysis

- **Time Complexity**:
   - Build: O(n).
   - Update: O(log n).
   - Query: O(log n).
  
- **Space Complexity**: O(n).

## Example Usage

```
data = [1,3,5,7,9,11]
seg_tree = SegmentTree(data)
print(seg_tree.query(1,4)) # Output: Sum of values in range [1,4) -> (3+5+7)
seg_tree.update(1,10) # Update index to value 10
print(seg_tree.query(1,4)) # Output after update.
```
