x, y = map(int,input().split())
z = list(map(int,input().split()))
A = []
for i in z:
    if i < y:
        A.append(i)
for i in A:
    print(i,end=' ')
print()