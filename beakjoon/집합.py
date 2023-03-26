n = int(input())
S = []

for i in range(n):
    x, y = input().split()
    x = str(x)
    y = int(y)
    if x == "add":
        S.append(y)
    if x == "remove":
        S.remove(y)
    if x == "check":
        for i in range(y):
            if S[i] == y:
                print(1)
        else:
            print(0)
    if x == "toggle":
        for i in range(y):
            if S[i] == y:
                print(1)
        else:
            S.append(y)
    if x == "all":
        S.clear()
        S.append(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    if x == "empty":
        S.clear()