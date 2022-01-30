# task 2

def rec_insertion_sort(array, index):
    if index <= 1:
        return -1
    rec_insertion_sort(array, index-1)
    x = index - 2
    y = array[index - 1]
    while (array[x] > y and x >= 0):
        array[x+1] = array[x]
        x -= 1
    array[x+1] = y


array = [6, 7, 8, 9, 4, 3, 2]
index = len(array)
rec_insertion_sort(array, index)
print(array)
