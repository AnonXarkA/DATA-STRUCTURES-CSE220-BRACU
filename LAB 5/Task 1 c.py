# c
def print_array(list, index):
    if index == len(list):
        return
    else:
        print(list[index])
        print_array(list, index+1)


list = [1, 2, 3, 4, 5, 7]
print_array(list, 0)
