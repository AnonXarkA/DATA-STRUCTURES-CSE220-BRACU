# task 3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyList:
    def __init__(self, a):
        self.head = None
        tail = None

        for x in a:
            new_node = Node(x)
            if self.head == None:
                self.head = new_node
                tail = new_node

            else:
                tail.next = new_node
                tail = new_node

    def showList(self):
        temp = self.head
        if temp is None:
            print("Empty List")
        else:
            while temp is not None:
                if temp.next is None:
                    print(temp.value)
                    break
                else:
                    print(temp.value, end=" ")
                    temp = temp.next

    def bubblesort(self):
        head = self.head
        tail = None
        if self.head is None:
            return
        else:
            while head != None:
                tail = head.next
                while tail != None:
                    if tail.value < head.value:
                        head.value, tail.value = tail.value, head.value
                    tail = tail.next
                head = head.next


array = [4, 7, 45, 9, 33, 2, 8]
linkedlist = MyList(array)
linkedlist.bubblesort()
linkedlist.showList()
