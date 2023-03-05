m = int(input())
n = int(input())
A = []
B = 0
for i in range(m,n+1):
    if i ** (1/2) % 1 == 0:
        A.append(i)
if A == []:
    print(-1)
else:
    for i in A:
        B += i
    print(B)
    print(min(A))