def customIter():
    for i in range(5):
        yield i

x = customIter()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

for i in x:
    print(i)