def Splitting_array(A):
    zero_list = [0]
    empty_list = []
    A_lentgh = len(A)
    logic = None
    for i in range(A_lentgh):
        if i == 0:
            zero_list[i] = A[i]
            empty_list = A[i+1:(A_lentgh)]
            if sum(zero_list) == sum(empty_list):
                logic = True
                break
            else:
                zero_list = []
                logic = False
        else:
            zero_list = A[0:i+1]
            empty_list = A[i + 1:(A_lentgh)]
            if sum(zero_list) == sum(empty_list):
                logic = True
                break
            else:
                logic = False
    print(logic)


A = [10, 3, 1, 2, 10]
Splitting_array(A)
