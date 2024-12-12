def linear_search(arr, target):
    # Traverse through the array
    for index, value in enumerate(arr):
        # Check if the current element matches the target
        if value == target:
            return index  # Return the index if found
    
    return -1  # Return -1 if the target is not found in the array
