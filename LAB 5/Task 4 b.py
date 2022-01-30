# b


def pattern(n):
    if n == 0:
        return 0
    else:
        pattern(n-1)
        print(n, end="")


def print_pattern(n, i):
    if n == 0:
        return 0
    else:
        space(n-1)
        pattern((i)-n+1)
        print()
        print_pattern(n-1, i)


def space(n):
    if n == 0:
        return 0
    else:
        space(n - 1)
        print("", end=" ")


print_pattern(6, 6)
