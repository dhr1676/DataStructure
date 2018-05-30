class Node(object):
    # 不用__init__也可以哎？？？
    left = None
    right = None
    parent = None
    key = None
    data = None


class Tree(object):

    def __init__(self):
        self._root = Node()
        self._root.left = Node()
        self._root.right = Node()
        self._root.parent = Node()
        self._root.data = None
        self._root.key = None

    def __MinNodeAux(self, node):
        while node.key and node.left.key:
            node = node.left
        return node

    def __SearchAux(self, data):
        node = self._root
        while node.key is not None:
            if node.data < data:
                node = node.right
            elif data < node.data:
                node = node.left
            else:
                return node
        print("Search node not found!")
        return None

    def __PrintAux(self, node):
        if node.key is None:
            return
        self.__PrintAux(node.left)
        print("Key is: %d, value is %d" % (node.key, node.data))
        if node.parent.key:
            print("Parent is %d" % node.parent.key)
        else:
            print("No parent, it is Root")
        if node.left.key:
            print("Left is %d" % node.left.key)
        else:
            print("No left child")
        if node.right.key:
            print("Right is %d" % node.right.key)
        else:
            print("No right child")
        print("")
        self.__PrintAux(node.right)

    # 为Delete服务，但是只处理了u,v跟parent节点的关系，child的关系都没管
    def __Transplant(self, u, v):
        if u.parent.key is None:
            self._root = v
        elif u.key == u.parent.left.key:
            u.parent.left = v
        else:
            u.parent.right = v
        if v.key:
            v.parent = u.parent

    def PrintTree(self):
        print("----------Print out the BST----------\n")
        self.__PrintAux(self._root)

    def Insert(self, key, data):
        node = Node()
        node.key = key
        node.data = data
        node.left = Node()
        node.right = Node()
        node.parent = Node()

        x = self._root
        y = Node()

        while x.key is not None:
            y = x
            if x.data > data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y.key is None:
            self._root = node
        elif y.data > data:
            y.left = node
        else:
            y.right = node

    def MinNode(self):
        node = self.__MinNodeAux(self._root)
        return node if node.key else None

    def Search(self, data):
        node = self.__SearchAux(data)
        return node if node.data else None

    def Delete(self, data):
        node = self.__SearchAux(data)

        if node is None:
            print("Delete node not found!")
            return None

        if node.left.key is None:
            self.__Transplant(node, node.right)
        elif node.right.key is None:
            self.__Transplant(node, node.left)
        else:
            succ = self.__MinNodeAux(node.right)
            if succ == node.right:
                # Transplant只解决parent，child得再做一次操作
                # 需要专门给被换的child做操作
                self.__Transplant(node, succ)
                succ.left = node.left
                succ.left.parent = succ
            else:
                self.__Transplant(node, succ)
                succ.right = node.right
                succ.right.parent = succ

        # Return
        data = node.data
        print("Delete node %d\n" % data)
        del node
        return data


if __name__ == '__main__':
    tree_1 = Tree()
    tree_1.Insert(4, 4)
    tree_1.Insert(2, 2)
    tree_1.Insert(1, 1)
    tree_1.Insert(3, 3)
    tree_1.Insert(5, 5)
    tree_1.Insert(6, 6)
    tree_1.PrintTree()

    print("Print out the Min node is %d\n" % tree_1.MinNode().key)
    #
    tree_1.Delete(4)
    tree_1.PrintTree()
