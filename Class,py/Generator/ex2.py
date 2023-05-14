from re import X


def customIter():
    x = range(5)
    yield from x

x = customIter()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
for i in x:
    print(i)