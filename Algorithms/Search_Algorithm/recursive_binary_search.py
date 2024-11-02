# An algorithm for recursive_binary_search
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

    if list[midpoint] == target:
        return True
    elif list[midpoint] > target:
        return recursive_binary_search(list[:midpoint], target)
    else:
        return recursive_binary_search(list[midpoint+1:], target)

def verify(results):
    print("Target Found: ", results)

numbers = [1,2,3,4,5,6,7,8,9]

result = recursive_binary_search(numbers, 6)

verify(result)