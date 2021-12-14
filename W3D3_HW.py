class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


NewList = List()
NewList.prepend(0)
NewList.append(1)
NewList.append(2)
NewList.append(3)
NewList.append(4)
NewList.prepend(5)
NewList.prepend(6)
NewList.prepend(7)
NewList.prepend(8)
NewList.prepend(9)
NewList.prepend(10)

NewList.print_list()
