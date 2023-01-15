n = int(input())
for i in range(n):
    c, v = map(int,input().split())
    x = c // v
    y = c % v
    print(f"You get {x} piece(s) and your dad gets {y} piece(s).")