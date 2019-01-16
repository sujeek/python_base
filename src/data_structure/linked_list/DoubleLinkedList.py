from src.pds.data_structure import DoubleNode

class DLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = DoubleNode(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def printlist(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

dllist = DLinkedList()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.printlist()