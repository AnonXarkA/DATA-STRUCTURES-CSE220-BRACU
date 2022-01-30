# task 3  [Medium]
def hocBuilder(height):
    if height == 0:
        return str(0) + "\nnot build a house at all."
    elif height == 1:
        return 8
    else:
        return 5+hocBuilder(height-1)


height = int(input("Enter height: "))
print(hocBuilder(height))
