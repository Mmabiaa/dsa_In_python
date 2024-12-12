def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, no need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr  # Return the sorted array
