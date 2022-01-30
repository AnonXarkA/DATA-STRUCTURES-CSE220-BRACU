# task 2  [Easy]
# a
def deci_to_binary(n):
    if n == 0:
        return 0
    else:
        return deci_to_binary(n//2)*10 + (n % 2)


decimal = deci_to_binary(11)
print(decimal)
