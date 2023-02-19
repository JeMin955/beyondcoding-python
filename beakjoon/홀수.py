x = []
y = []
z = 0
for i in range(0, 7):
    n = int(input())
    if n % 2 == 0:
        y.append(n)
    else:
        x.append(n)
if len(x) == 0:
    print(-1)
else:
    for i in x:
        z += i
    print(z)
    print(min(x))