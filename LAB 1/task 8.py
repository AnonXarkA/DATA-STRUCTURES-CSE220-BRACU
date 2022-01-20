# 8 Repetition

def repetition(new_array):
    new_list = []
    dictionary = {x: new_array.count(x) for x in new_array}
    for keys, values in dictionary.items():
        if values > 1:
            new_list.append(values)
    if len(new_list) == len(set(new_list)):
        print("False")
    else:
        print("True")


new_array = [4, 5, 6, 6, 4, 3, 6, 4]
repetition(new_array)
