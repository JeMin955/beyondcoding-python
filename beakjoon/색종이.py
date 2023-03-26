xx = []
yy = []
zz = []
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    xx.append(x + 10)
    yy.append(y + 10)
for i in range(len(xx)):
    for j in range(len(yy)):
        zz.append(xx[i] + yy[j])
print(zz)