x = list(map(int,input().split()))
y = []
z = 0
for i in x:
    y.append(i * i)
for i in y:
    z += i
print(z % 10)