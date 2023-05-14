x = list(map(int,input().split()))
l = max(x)
for i in range(max(x)):
    for j in range(len(x)):
        if l > x[j]:
            print(" ", end="")
        else:
            print("*", end="")

    l -= 1
    print()