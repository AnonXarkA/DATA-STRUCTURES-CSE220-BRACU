# task 4

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

    def selection_sort(self):
        head = self.head
        if self.head is None:
            return
        else:
            while head.next != None:
                tail = head
                val = head.value
                next_val = head.next
                while next_val != None:
                    if val > next_val.value:
                        val = next_val.value
                        tail = next_val
                    next_val = next_val.next
                head.value, tail.value = tail.value, head.value
                head = head.next


array = [4, 7, 45, 9, 33, 2, 8]
linkedlist = MyList(array)
linkedlist.selection_sort()
linkedlist.showList()
