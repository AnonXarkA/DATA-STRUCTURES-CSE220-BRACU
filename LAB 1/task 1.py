def shiftLeft(source, k):
    index = len(source)  # total index of array
    for v in range(index):
        x = v - k
        if x >= 0:
            source[x] = source[v]

    remain_index = len(source) - k
    for v in range(remain_index, index):
        source[v] = 0

    print(source)


source = [10, 20, 30, 40, 50, 60]

shiftLeft(source, 3)
