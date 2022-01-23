# task 3


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createlinkedlist(self, num_of_nodes):
        node_inputs = int(input("Enter node values: "))
        x = 0
        tail = None
        self.lenght = 0
        while x < num_of_nodes:
            if x == 0:
                self.head = Node(node_inputs)
                tail = self.head
            else:
                new_node = Node(int(input("Enter node values: ")))
                tail.next = new_node
                tail = new_node
            x = x + 1
            self.lenght += 1

    def showlist(self):
        temp = self.head
        if temp is None:
            print("Empty list")
        else:
            while temp is not None:
                if temp.next is None:
                    print(temp.value)
                    break
                else:
                    print(temp.value, end=" -> ")
                    temp = temp.next

    def even_number(self):
        temp = self.head
        new_head = None
        tail = None
        while temp is not None:
            if temp.value % 2 == 0:
                new_node = Node(temp.value)
                if new_head == None:
                    new_head = new_node
                    tail = new_node
                else:
                    tail.next = new_node
                    tail = tail.next
            temp = temp.next
        tail = new_head
        while True:
            if tail.next is None:
                print(tail.value)
                break
            else:
                print(tail.value, end=" -> ")
                tail = tail.next

    def find_out(self, value):
        temp = self.head
        statement = None
        while temp.next is None:
            if temp.value == value:
                statement = True

        if statement == True:
            print("True")
        else:
            print("False")

    def reverse(self):
        temp = self.head
        before = None
        while temp != None:
            tail = temp.next
            temp.next = before
            before = temp
            temp = tail
        self.head = before

    def sort(self):
        self.temp = self.head
        self.value = None

        if (self.head == None):
            print("empty List")
        else:
            for val in range(self.lenght):
                if self.temp is not None:
                    self.value = self.temp.next

                    for val in range(self.lenght - 1):
                        if self.value is not None:
                            if (self.temp.value > self.value.value):
                                cur = self.temp.value
                                self.temp.value = self.value.value
                                self.value.value = cur
                            self.value = self.value.next
                    self.temp = self.temp.next

    def sum(self):
        new = self.head
        total_sum = 0
        while new is not None:
            total_sum += new.value
            new = new.next
        print(total_sum)

    def rotate(self, rotate_position, k):
        if rotate_position == "left":
            for x in range(k):
                temp = self.head
                self.head = self.head.next
                temp.next = None
                position = self.head
                while position.next != None:
                    position = position.next
            position.next = temp

        elif rotate_position == "right":
            for x in range(k):
                temp = None
                position = self.head
                while position.next.next != None:
                    position = position.next
                temp = position.next
                position.next = None
            temp.next = self.head
            self.head = temp
        else:
            print("Invalid")


list1 = MyList()
list2 = list1
list1.createlinkedlist(int(input("Please Enter the Number of Nods: ")))
list1.showlist()
list1.even_number()
list1.find_out(7)
list1.reverse()
list1.showlist()
list1.sort()
list1.showlist()
list1.sum()
list2.rotate("left", 2)
list2.showlist()
