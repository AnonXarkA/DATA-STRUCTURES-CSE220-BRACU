def removeAll(source, size, elements):
    source_index = len(source)
    new_list = [0] * source_index
    x = 0
    for values in source:
        if values == elements:
            continue
        else:
            new_list[x] = values
        x += 1
        if x >= size:
            break
    source = new_list
    print(source)


source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 2)
