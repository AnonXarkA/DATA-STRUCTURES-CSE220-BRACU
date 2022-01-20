# 2 Intersection
def intersection(array_1, start1, size1, array_2, start2, size2):
    new_list1 = []
    new_list2 = []
    new_list3 = []
    new_list4 = []
    new_list5 = []
    array1_lenght = len(array_1)
    array2_lenght = len(array_2)
    for values in range(1, array1_lenght):
        if array_1[values] == 0 and array_1[values-1] != 0:
            for x in range(values):
                new_list1.append(array_1[x])

    for value in range(1, array1_lenght):
        if array_1[value] != 0 and array_1[value - 1] == 0:
            for x in range(value, array1_lenght):
                new_list2.append(array_1[x])

    for values in range(1, array2_lenght):
        if array_2[values] == 0 and array_2[values-1] != 0:
            for y in range(values):
                new_list3.append(array_2[y])

    for value in range(1, array2_lenght):
        if array_2[value] != 0 and array_2[value - 1] == 0:
            for y in range(value, array2_lenght):
                new_list4.append(array_2[y])

    combined_list1 = new_list2 + new_list1
    combined_list2 = new_list4 + new_list3

    for value in range(len(combined_list1)):
        new = combined_list1[value]
        for values in range(len(combined_list2)):
            if new == combined_list2[values]:
                if new not in new_list5:
                    new_list5.append(new)
                else:
                    continue
            else:
                continue
    print(new_list5)


intersection([40, 50, 0, 0, 0, 10, 20, 30], 5, 6, [
             10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25], 8, 7)
