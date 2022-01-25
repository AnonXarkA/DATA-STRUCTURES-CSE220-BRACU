# Task 1

stack = []
index = []
openingbrackets = ["[",'{',"("]
closingbrackets = ["]","}",")"]


def paranthesis_balancing(string):
    t = 0
    expression = True
    for x in range(0,len(string)):
        if string[x] in openingbrackets or string[x] in closingbrackets:
            if string[x] in openingbrackets:
                stack.append(string[x])
                index.append(x+1)
            else:
                if len(stack) == 0 and string[x] in closingbrackets:
                    t = string[x]
                    index.append(x+1)
                    expression = False
                    break
                t = stack.pop()
                expression = bracket_checking(t,string[x])
                if expression == True:
                    index.pop()
    

    if expression is True:
        print("This expression is correct.")
        
        
    else:
        if len(stack) != 0:
            print('This expression is NOT correct.')
            print("Error at character # {0}. '{1}'- not closed.".format(index[-1], t))
        
        else:
            if expression is False: 
                print('This expression is NOT correct.')
                print("Error at character # {0}. '{1}'- not opened.".format(index[0], t))

            

            

def bracket_checking(a,b):
    if a == "(" and b == ")":
        return True
    elif a == "{" and b == "}":
        return True
    elif a == "[" and b =="]":
        return True
    else:
        return False

string = input()
paranthesis_balancing(string)
