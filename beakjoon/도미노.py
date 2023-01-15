n = int(input())
x = 0
for i in range(1,n+1):
    if i == 1:
        x += 3
    else:
        for j in range(i, i+i+1):
            x += j
print(x)