# task 6

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


def sameornot(tree_node1, tree_node2):

    if tree_node1 == None and tree_node2 == None:
        return True

    if tree_node1 and tree_node2 is not None:
        return tree_node1.data == tree_node2.data and sameornot(tree_node1.left, tree_node2.left) and sameornot(tree_node1.right, tree_node2.right)

    return False


root = Node(1)
second_node = Node(2)
thrd_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)
root.left = second_node
root.right = thrd_node
thrd_node.left = fourth_node
thrd_node.right = fifth_node
sixt_node = Node(6)
seven_node = Node(7)
eight_node = Node(8)
fifth_node.left = sixt_node
fifth_node.right = seven_node
seven_node.left = eight_node


root2 = Node(1)
second_node2 = Node(2)
thrd_node2 = Node(3)
fourth_node2 = Node(4)
fifth_node2 = Node(5)
root2.left = second_node2
root2.right = thrd_node2
thrd_node2.left = fourth_node2
thrd_node2.right = fifth_node2
sixt_node2 = Node(6)
seven_node2 = Node(7)
eight_node2 = Node(8)
fifth_node2.left = sixt_node2
fifth_node2.right = seven_node2
seven_node2.left = eight_node2


if sameornot(root, root2) is True:
    print("Both two trees are exactly same")
else:
    print("two trees are not exactly same")
