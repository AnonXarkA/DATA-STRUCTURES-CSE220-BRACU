# task 1

class Node:
    def __init__(self, data, parent_node, left, right):
        self.data = data
        self.parent_node = parent_node
        self.left = left
        self.right = right


class binarytree:
    def __init__(self):
        self.root = Node(1, None, None, None)
        self.second_node = Node(2, self.root, None, None)
        self.thrd_node = Node(3, self.root, None, None)
        self.fourth_node = Node(4, self.thrd_node, None, None)
        self.fifth_node = Node(5, self.thrd_node, None, None)
        self.sixt_node = Node(6, self.fifth_node, None, None)
        self.seven_node = Node(7, self.fifth_node, None, None)
        self.root.left = self.second_node
        self.root.right = self.thrd_node
        self.thrd_node.left = self.fourth_node
        self.thrd_node.right = self.fifth_node
        self.fifth_node.left = self.sixt_node
        self.fifth_node.right = self.seven_node

    def maximum(self, first, second):
        if second <= first:
            return first
        else:
            return second

    def height(self, root):

        if root is None:
            return 0

        return 1 + self.maximum(self.height(root.left), self.height(root.right))


tree = binarytree()

print(" Height : ", tree.height(tree.root))
