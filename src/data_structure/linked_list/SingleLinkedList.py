from src.pds.data_structure import  Node



class SLinkedList:
    def __init__(self):
        self.headval = None

    def traversal(self):
        phead = self.headval
        while phead is not None:
            print(phead.data)
            phead = phead.nextval
    def insertStart(self, data):
        headNode = Node(data)
        headNode.nextval = self.headval
        self.headval = headNode

    def insertEnd(self, data):
        endNode = Node(data)
        if self.headval is None:
            self.headval = endNode
            return
        end = self.headval
        while end.nextval:
            end = end.nextval
        end.nextval = endNode

    def insert(self, currentNode, data):
        newNode = Node(data)
        newNode.nextval = currentNode.nextval
        currentNode.nextval = newNode

    def remove(self, data):
        temp = self.headval
        if temp is not None:
            if temp.data == data:
                self.headval = self.headval.nextval
                return
        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.nextval
        if temp is None:
            return
        prev.nextval = temp.nextval

        temp = None

# list1 = SLinkedList()
# list1.headval = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
#
# list1.headval.nextval = n2
# n2.nextval = n3
# n3.nextval = n4
# n4.nextval = n5

# list1.traversal()

# list1.insertStart(0)
# list1.traversal()
# list1.insertEnd(6)
# list1.insertEnd(7)

list1 = SLinkedList()
list1.insertEnd(1)
list1.insertEnd(2)
list1.insertEnd(3)
list1.insertEnd(4)
list1.insertEnd(5)
list1.insert(list1.headval, 6)

list1.traversal()

print("------------------------")
list1.remove(4)
list1.traversal()