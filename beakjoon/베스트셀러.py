import sys
input = sys.stdin.readline
n = int(input())
y = []
z = {}
v = []

for i in range(n):
    x = input().strip()
    y.append(x)
    X = y.count(x)
    z.update({x:X})
for i,j in z.items():
    if max(z.values()) == j:
        v.append(i)
v.sort()
print(v[0])