class Zemeen:
    def __init__(self, stop):
        self.current = 0
        self.stop = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            res = self.current
            self.current += 1
            return res
        else:
            raise StopIteration

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

z = Zemeen(3)
print(z[2], z[0])

# z = Zemeen(5)
# x = list(range(5))

# for i in z:
#     print(i, end = " ")
# for i in x:
#     print(i, end = " ")