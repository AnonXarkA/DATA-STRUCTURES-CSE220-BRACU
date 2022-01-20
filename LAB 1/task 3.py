def remove(source, size, idx):
    source_index = len(source)
    new_list = source_index * [0]
    x = 0
    for values in range(size):
        if values == idx:
            continue
        else:
            new_list[x] = source[values]
            x += 1

    source = new_list

    print(source)


source = [10, 20, 30, 40, 50, 0, 0]

remove(source, 5, 2)
