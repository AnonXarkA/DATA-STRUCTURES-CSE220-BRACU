# task 2

class Node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def get_level(node, data, l):
    if node is None:
        return 0
    if data == node.data:
        return l

    leveld = get_level(node.left, data, l + 1)
    if leveld != 0:
        return leveld

    leveld = get_level(node.right, data, l + 1)
    return leveld


def getlevel(node, data):
    return get_level(node, data, 1)


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

print(f"LEVEL: {getlevel(root,8)}")
