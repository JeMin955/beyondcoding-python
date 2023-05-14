x, y = map(int,input().split())
A = list()
a = list()
b = list()
for i in range(x):
    Se = list(map(int,input().split()))
    A.append(Se)
for i in range(x):
    Se = list(map(int,input().split()))
    a.append(Se)
for i in range(x):
    c = []
    for j in range(y):
        z = A[i][j] + a[i][j]        
        c.append(z)
    b.append(c)
for i in b:
    print(*i)