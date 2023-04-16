s = int(input())
PM = 0
for i in range(s):
    if not i == 1:
        f = 0  
        for j in range(2, i):
            if i % j == 0:
                f+=1
        if f == 1:
            PM += i
print()