n = int(input())
x = list(map(int,input().split()))
y = [x[0]]
z = 0
for i in range(1, len(x)):
    if x[i] == 1:
        if x[i - 1] == x[i]:
            y.append(y[i-1] + 1)
        else:
            y.append(1)
    else:
        y.append(0)

print(sum(y))