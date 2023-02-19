n = int(input())
x = 0
a, b, c, d, e = map(int,input().split())
if a == n:
    x += 1
if b == n:
    x += 1
if c == n:
    x += 1
if d == n:
    x += 1
if e == n:
    x += 1
print(x)