def array_series(n):
    n_squared = n*n
    new_array = [0]*n_squared

    x = 1
    while x <= n:
        y = 1
        while y <= x:
            new_array[(x*n)-y] = y

            y += 1
        x += 1
    return new_array


n = int(input("Please input a number: n= "))
print(array_series(n))
