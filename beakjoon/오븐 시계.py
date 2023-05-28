x, y = map(int,input().split())
z = int(input())
f = y + z
if z > 59:
    while f >= 60:
        f -= 60
        x += 1
print(x, f)