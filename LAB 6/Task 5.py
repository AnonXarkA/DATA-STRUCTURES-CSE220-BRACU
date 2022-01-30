# task 5

class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class Doublylinkedlist:
    def __init__(self, array):
        self.head = Node(array[0], None, None)
        tail = self.head
        for x in range(1, len(array)):
            new_node = Node(array[x], None, tail)
            tail.next = new_node
            tail = new_node

    def showList(self):
        if self.head.next is None:
            print("Empty list")
        else:
            head = self.head
            while self.head is not None:
                if head.next is None:
                    print(head.value)
                    break
                else:
                    print(head.value, end=" ")
                    head = head.next

    def insertion_sort(self):
        head = self.head
        if head == None:
            return
        else:
            while head is not None:
                tail = head.next
                while tail and tail.prev != None and tail.value < tail.prev.value:
                    tail.value, tail.prev.value = tail.prev.value, tail.value
                    tail = tail.prev
                head = head.next


array = [7, 6, 9, 3, 5, 99, 1]
doublylinkedlist = Doublylinkedlist(array)
doublylinkedlist.insertion_sort()
doublylinkedlist.showList()
