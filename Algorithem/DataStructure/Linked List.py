class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        dummy = self.Node(None)
        self.head = dummy
        self.tail = dummy

    def push(self, data):
        self.tail.next = self.Node(data)
        self.tail = self.tail.next
        #node = self.head
        #while node.next:
        #    node = node.next
        #node.next = Node(data)
            
    def pop(self):
        node = self.head
        before = None
        while node.next:
            before = node
            node = node.next
        data = node.data
        before.next = None
        return data

    def size(self):
        sz = 0
        node = self.head
        while node.next:
            node = node.next
            sz += 1
        return sz

linkedList = LinkedList()

linkedList.size()
linkedList.push(1)
print(linkedList.size())