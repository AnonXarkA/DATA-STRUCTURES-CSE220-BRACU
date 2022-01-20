# Circular Array
# 1 Palindrome


def palindrome(array, start, size):
    empty_list = []
    start_num = start
    array_lenght = len(array)
    for values in range(size):
        if array[start_num] != 0:
            empty_list.append(array[start_num])
            start_num += 1
        if start_num == array_lenght:
            start_num = 0
    logic = (len(empty_list)+1)//2
    if empty_list[0:logic] == empty_list[-1:-(logic+1):-1]:
        print("True")
    else:
        print("False")


array = [20, 10, 0, 0, 0, 10, 20, 30]
palindrome(array, 5, 5)
