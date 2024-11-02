# An algorithm for binary_searching
def binary_search(list, target):
    first = 0
    last = len(list) - 1 # index starts at 0 so we subtract 1 from the length to get the last.

    while first <= last:
        midpoint = (first + last) // 2 # obtaining the index of the elements

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None: # If the index is inclusive...
        print("Target found at index: ", index)
    else: # If the index is not found...
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)