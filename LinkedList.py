class Node(object):

    def __init__(self, value=0, next = None):
        self.data = value
        self.__next = next


class LinkedList(object):

    def __init__(self):
        self.head = 0

    def __del__(self):
        print("Linked List has been destroyed!")

    def getNode(self, key):

        if self.head is None:
            print("Linked list is empty")
            return None
        else:
            return self.getNode(key)

    @property
