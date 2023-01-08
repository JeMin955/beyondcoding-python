class Queue:
    def __init__(self):
        self.items = []
    
    def put(self, item):
        self.items.append(item)

    def get(self):
        return self.items.pop(0)
     
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

    def IsEmpty(self):
        return self.size() == 0

queue = Queue()

for _ in range(5):
    queue.put(input())

while not queue.IsEmpty():
    print(queue.get(), end=' ')