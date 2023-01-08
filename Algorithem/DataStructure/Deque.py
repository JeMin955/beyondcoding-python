class Deque:

    def __init__(self):
        self.items = []

    def pushleft(self, item):
        self.items.insert(0, item)

    def popright(self):
        return self.items.pop()

    def peekright(self):
        return self.items[-1]

    def __init__(self):
        self.items = []
    
    def pushright(self, item):
        self.items.append(item)

    def popleft(self):
        return self.items.pop(0)
     
    def peekleft(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def IsEmpty(self):
        return self.size() == 0

Deque = Deque()

for _ in range(5):
    Deque.pushleft(input())

while not Deque.IsEmpty():
    print(Deque.popleft(), end=' ')