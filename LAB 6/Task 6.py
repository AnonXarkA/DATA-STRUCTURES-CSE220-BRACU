# task 6

def rec_binary_search(array, left, right, value):
    if left > right:
        return -1
    else:
        mid_value = int((left+right) // 2)
        if array[mid_value] < value:
            return rec_binary_search(array, mid_value+1, right, value)
        elif array[mid_value] > value:
            return rec_binary_search(array, left, mid_value-1, value)
        else:
            return mid_value


array = [1, 2, 3, 4, 5, 6, 7]
left = 0
right = len(array)
value = 6
print(rec_binary_search(array, left, right, value))
