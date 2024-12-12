def binary_search(arr, target):
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    
    # Continue searching while the left pointer is less than or equal to the right pointer
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        
        # Check if the target is present at mid
        if arr[mid] == target:
            return mid  # Return the index if found
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not found in the array
