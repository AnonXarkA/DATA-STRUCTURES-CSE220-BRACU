# 7 Max Bunch Count

def Max_Bunch_Count(new_array):
    sum_list = []
    first = new_array[0]
    c = 0
    for values in new_array:
        if values == first:
            c += 1

        else:
            first = values
            c = 1
        sum_list.append(c)
    print(max(sum_list))


new_array = [1, 2, 2, 3, 4, 4, 4]
Max_Bunch_Count(new_array)
