class Node(object):

    def __init__(self, left=None, right=None, parent=None, key=None, data=None):
        self._left = left
        self._right = right
        self._parent = parent
        self._key = key
        self._data = data


class Tree(object):

    def __init__(self):
        self._root = Node(None)

    def MinAux(self, node):
        return None

    def SearchAux(self, key):
        return None

    def PrintAux(self, node):
        if node is None:
            return

        self.PrintAux(node.left)
        print("\n")
        print("Key: ", end="")

        return None

    def Transplant(self, u, v):
        return None

    def PrintTree(self):
        return

    def Insert(self, key, data):
        return

    def MinNode(self):
        return

    def Search(self, key):
        return

    def Delete(self, key):
        return
