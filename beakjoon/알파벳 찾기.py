x = input()
y = 'abcdefghijklmnopqrstuvwxyz'
z = list()
for i in y:
    if i in x:
        z.append(x.index(i))
    else:
        z.append(-1)
print(*z)