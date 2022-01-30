# task 1

def rec_selection_sort(array, x, y):
    index = len(array)
    if x < index-1:
        min_index = x
        rec_selection_sort(array, x + 1, x + 2)
        if y < index:
            if array[y] < array[min_index]:
                min_index = y
            rec_selection_sort(array, x, y+1)
        array[x], array[min_index] = array[min_index], array[x]


array = [5, 7, 9, 8, 2, 1]
rec_selection_sort(array, 0, 1)
print(array)
