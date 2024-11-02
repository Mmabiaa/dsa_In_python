# An algorithm for linear search
def linear_search(list, target):
    # Return the index of the target if found, else return none.
    length = len(list)
    for i in range(0, length):
        if list[i] == target:
            return i
    return None

#A function to verify the linear_search function.
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)

