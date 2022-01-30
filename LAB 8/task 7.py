# task 7

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def copy_tree(node):
    if node == None:
        return
    else:
        print(node.data)
        copy_tree(node.left)
        copy_tree(node.right)
        node.left, node.right = node.right, node.left


root = Node(1)
second_node = Node(2)
thrd_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
sixt_node = Node(6)
seven_node = Node(7)
eight_node = Node(8)
root.left = second_node
root.right = thrd_node
thrd_node.left = fourth_node
thrd_node.right = fifth_node
fifth_node.left = sixt_node
fifth_node.right = seven_node
seven_node.left = eight_node

copy_tree(root)
