m = 15
x = []
for i in range(5):
    n = list(input())
    N = len(n)
    if N < m:
        for i in range(N, m-N):
            n.append(".")
    x.append(n)
print(x)