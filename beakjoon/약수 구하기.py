x = []
for i in range(9):
    n = int(input())
    x.append(n)
print(max(x))
print(x.index(max(x))+1)