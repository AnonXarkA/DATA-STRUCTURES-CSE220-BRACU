# Task 1 [Very Easy]
# a

def factorial(n):
    if n == 0 | n == 1:
        return 1
    else:
        return n * factorial(n-1)


fact = factorial(6)
print(fact)
