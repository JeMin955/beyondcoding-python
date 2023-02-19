y = []
n = int(input())
for i in range(n):
    t = int(input())
    x = list(map(int,input().split()))
    z = 0
    for j in x:
        z += j
    y.append(z)
for i in y:
    print(i)