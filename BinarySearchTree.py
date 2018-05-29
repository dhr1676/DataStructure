class Node(object):

    def __init__(self, key=None, data=None):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.data = data


class Tree(object):

    def __init__(self):
        self._root = Node(None)

    def MinAux(self, node):
        return None

    def SearchAux(self, key):
        return None

    def __PrintAux(self, node):
        if node is None:
            return

        self.__PrintAux(node.left)
        print("Key is: %d, value is %d\n" % (node.key, node.data))
        self.__PrintAux(node.right)

    def Transplant(self, u, v):
        return None

    def PrintTree(self):
        self.__PrintAux(self._root)
        return

    def Insert(self, key, data):
        node = Node()
        node.key = key
        node.data = data

        x = self._root
        y = None
        while x.key is not None:
            y = x
            if x.data > data:
                x = x.left
                print(type(x))
            else:
                x = x.right
                print(type(x))


        node.parent = y
        if y is None:
            self._root = node
        elif y.data > data:
            y.left = node
        else:
            y.right = node

    def MinNode(self):
        return

    def Search(self, key):
        return

    def Delete(self, key):
        return


if __name__ == '__main__':
    tree = Tree()
    tree.Insert(1, 1)
    tree.Insert(2, 2)
    # tree.Insert(3, 3)
    # tree.Insert(4, 4)
    # tree.Insert(5, 5)
    # tree.Insert(6, 6)
    tree.PrintTree()
