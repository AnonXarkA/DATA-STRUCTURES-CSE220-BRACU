# b
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

    def sum_add(self, head):
        if head is None:
            return 0
        else:
            return head.value + self.sum_add(head.next)

    def sum(self):
        return self.sum_add(self.head)


array = [1, 2, 3, 4, 5, 6, 7]
listlinked = linklist(array)
print(listlinked.sum())
