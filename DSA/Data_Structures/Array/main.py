def insert(arr, index, value):
    """Insert an element at a specific index."""
    arr.insert(index, value)
    return arr

def delete(arr, index):
    """Delete an element from the specified index."""
    if 0 <= index < len(arr):
        arr.pop(index)
    return arr

def search(arr, value):
    """Search for an element and return its index."""
    try:
        return arr.index(value)
    except ValueError:
        return -1

def update(arr, index, value):
    """Update an element at a specific index."""
    if 0 <= index < len(arr):
        arr[index] = value
    return arr

def traverse(arr):
    """Traverse and print all elements in the array."""
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)

# Insertion
arr = insert(arr, 2, 10)
print("After Insertion:", arr)

# Deletion
arr = delete(arr, 3)
print("After Deletion:", arr)

# Searching
index = search(arr, 10)
print("Index of 10:", index)

# Update
arr = update(arr, 1, 20)
print("After Update:", arr)

# Traversing
print("Traversed Array:", traverse(arr))
