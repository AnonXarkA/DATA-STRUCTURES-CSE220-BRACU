# c
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class linklist:
    def __init__(self, array):
        self.head = None
        tail = None
        for x in array:
            new_node = Node(x)
            if self.head == None:
                self.head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

    def reverse(self, head):
        if head.next is None:
            print(head.value)
        else:
            self.reverse(head.next)
            print(head.value)

    def reverse_print(self):
        return self.reverse(self.head)


array = [1, 2, 3, 4, 5, 6, 7]
listlinked = linklist(array)
listlinked.reverse_print()
