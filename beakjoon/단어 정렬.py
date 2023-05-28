import sys
input = sys.stdin.readline
n = int(input())
y = []

for i in range(n):
    x = input().strip()
    y.append(x)

y = list(set(y))
y.sort()
y.sort(key=len)
for i in range(len(y)):
    print(y[i]) 