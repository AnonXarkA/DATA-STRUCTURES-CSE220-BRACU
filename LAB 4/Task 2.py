# Task 2


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,element):
        if self.head == None:
            self.head = Node(element)
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(element)

    def pop(self):
        global list_status
        global available
        if self.head == None:
            list_status = "Empty"
            available = None
        else:
            if self.head.next == None:
                available = self.head.data
                self.head = None
            else:
                n = self.head
                while n.next.next is not None:
                    n = n.next
                available = n.next.data
                n.next = None




openingrackets = ["[",'{',"("]
closingrackets = ["]","}",")"]

def bracket_checking(a,b):
    if a == "(" and b == ")":
        return True
    elif a == "{" and b == "}":
        return True
    elif a == "[" and b == "]":
        return True
    else:
        return False

check = linkedlist()
string = input()
expression = False
index = []
t = 1
x = 0
y = ""

for v in string:
    if v in openingrackets:
        check.push(v)
        index.append(t)
    if v in closingrackets:
        check.pop()
        if available == None:
            expression = False
            x = t
            y = v
            break
        else:
            expression = bracket_checking(available,v)
            if expression == True:
                index.pop()
            else:
                x = index
                y = available
    t = t+1

if expression is True:
    print('This expression is correct.')
else:
    if isinstance(x,list):        #The isinstance() function returns True if the specified object is of the specified type, otherwise False
        print('This expression is NOT correct.')
        print("Error at character # {0}. '{1}'- not closed.".format(x[-1], y))
    else:
        print('This expression is NOT correct.')
        print("Error at character # {0}. '{1}'- not opened.".format(x, y))
