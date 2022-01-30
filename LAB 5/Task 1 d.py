# d
def powerN(base, n):
    if n == 0:
        return 1
    else:
        return base*powerN(base, n-1)


power = powerN(3, 3)
print(power)
