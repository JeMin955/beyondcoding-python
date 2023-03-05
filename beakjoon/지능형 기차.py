A = []
z = 0
for i in range(4):
    x, y = map(int,input().split())
    z -= x
    z += y
    A.append(z)
print(max(A))