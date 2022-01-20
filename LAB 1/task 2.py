def rotateLeft(source, k):
    list_lenght = len(source)
    for values in range(k):
        new_value = source[0]
        for value in range(1, list_lenght):
            source[value - 1] = source[value]
        source[list_lenght - 1] = new_value


source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)
print(source)
