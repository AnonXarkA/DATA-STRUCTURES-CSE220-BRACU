# task 7
arr = [-1]*99


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        if arr[n] == -1:
            arr[n] = fibonacci(n-1) + fibonacci(n-2)
        return arr[n]


fi = fibonacci(12)
print(fi)
