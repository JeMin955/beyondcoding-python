import sys
input = sys.stdin.readline
n = int(sys.stdin.readline())
z = 1
for i in range(n):
    h = int(sys.stdin.readline())
    z += h
    z -= 1
print(z)