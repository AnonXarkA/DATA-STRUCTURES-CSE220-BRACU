# task 4 [Hard]
# a

def pattern(n):
    if n == 0:
        return 0
    else:
        pattern(n-1)
        print(n, end="")


def print_pattern(n):
    if n == 0:
        return 0
    else:
        print_pattern(n-1)
    pattern(n)
    print()


n = int(input("Enter n: "))

print_pattern(n)
