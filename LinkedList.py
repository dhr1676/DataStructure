class Node(object):

    def __init__(self, value=0, p=None):
        self.data = value
        self.next = p


class LinkedList(object):

    def __init__(self):
        self.head = None

    def buildList(self, data):

        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getSize(self):
        now = self.head
        size = 0
        while now:
            size += 1
            now = now.next

        return size

    def is_empty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def clearList(self):
        self.head = 0
        print("List is empty now!")

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            return

    # Insert a node in a specific position
    def insert(self, index, value):
        if index < 0 or index > self.getSize():
            print("Invalid index")
            return

        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        else:
            pos = 0
            dummy = Node(-1)
            dummy.next = self.head
            p = dummy
            while p.next and pos < index:
                p = p.next
                pos += 1

            node.next = p.next
            p.next = node
            return

    # Remove a node by key
    def remove(self, key):
        if self.is_empty():
            raise ValueError("Empty list!")

        dummy = Node(-1)
        dummy.next = self.head
        temp = dummy

        while temp and temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                print("Remove node %d\n" % key)
                return
            else:
                temp = temp.next

        print("Node not found")
        return None

    # Get a node by the key
    def getNode(self, key):

        if self.is_empty():
            print("List is empty")
            return None

        temp = self.head
        index = 1
        while temp:
            if key == temp.data:
                return index
            temp = temp.next
            index += 1

        print("Node not found")
        return None

    # Traverse and print out the list
    def printList(self):
        if self.is_empty():
            print("Empty list!")
            return

        temp = self.head
        print("The list is: ", end="")
        while temp:
            print("%d" % temp.data, end="")
            if temp.next:
                print(" --> ", end="")
            temp = temp.next
        print("\n")


if __name__ == '__main__':
    input_data = [1, 3, 5, 7, 9]
    print(input_data)

    # Test build linkedlist
    link_list = LinkedList()
    link_list.buildList(input_data)
    link_list.printList()

    # Test get node
    print("3 is the %d element\n" % link_list.getNode(3))

    # Test remove node
    link_list.remove(3)
    link_list.printList()

    # Test insert node
    print("Insert 3 at the previous position\n")
    link_list.insert(1, 3)
    link_list.printList()
    print("Insert 4 between 3 and 5")
    link_list.insert(2, 4)
    link_list.printList()

    link_list.insert(6, 11)
    link_list.printList()

    link_list.clearList()
    link_list.printList()

    l_list = LinkedList()
    l_list.append(1)
    l_list.append(2)
    l_list.append(3)
    l_list.printList()
