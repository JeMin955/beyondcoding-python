x = []
z = []
for i in range(9):
    l = list(map(int, input().split()))
    z.append(l)
    
    x.append(l[l.index(max(l))])

m = max(x)
row = x.index(m)
col = z[row].index(m)

print(m)
print(row + 1)
print(col + 1)