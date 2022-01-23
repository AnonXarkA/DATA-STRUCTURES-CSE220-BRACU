# Task 2


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
            if (self.head == None):
                self.head = new_node
                tail = new_node

            else:
                tail.next = new_node
                tail = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

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
                    print(temp.value, end=" -> ")
                    temp = temp.next

    def isEmpty(self):
        temp = self.head
        statement = None
        if temp is None:
            statement = True
        else:
            statement = False
        print(statement)

    def clear(self):
        temp = self.head
        while temp is not None:
            temp.value = None
            temp = temp.next
        self.head = None

    def insert(self, newElement):
        new_node = Node(newElement)
        counter = None
        if self.head == None:
            self.head = new_node
        tail = self.head
        while True:
            if tail.next is None:
                break
            if tail.value == newElement:
                counter = True
            tail = tail.next
        if counter is True:
            print("Key already exists")
        else:
            tail.next = new_node

    def insert_index(self, newElement, index):
        temp = self.head
        counter = 1
        while counter < index-1 and temp is not None:
            temp = temp.next
            counter = counter + 1
        if temp is None:
            print("key already exists and does not insert the key")
        else:
            new_node = Node(newElement)
            new_node.next = temp.next
            temp.next = new_node

    def remove(self, values):
        temp = None
        if self.head == values:
            self.head = self.head.next
            temp = str(self.head)
            str_value = temp+"was removed from the linked list"
            return str_value
        else:
            temp1 = self.head
            while temp1.next is not None:
                if temp1.next.value == values:
                    temp = temp1.next.value
                    break
                temp1 = temp1.next
            if temp1.next is None:
                print("Element doesn't exist")
            else:
                temp1.next = temp1.next.next
                print(temp, "was removed from the linked list")


a = [10, 20, 30, 40]
a2 = []
list1 = MyList(a)
list2 = MyList(a2)
list1.showList()
list2.showList()
list1.isEmpty()
list2.isEmpty()
list1.insert(50)
list1.showList()
list1.insert(10)
list1.insert_index(60, 5)
list1.showList()
list1.remove(20)
list1.showList()
list1.clear()
list1.showList()
