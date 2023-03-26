N = int(input())

x = list(map(int,input().split()))
# y = []
# z = []

# for i in x:
#     if i > N:
#         y.append(i)
#         z.append(i-N)
#     elif i < N:
#         y.append(i)
#         z.append(N-i)
#     elif i == N:
#         print(i)
#         break


# print(y[z.index(min(z))])

m = 999999999
r = 0

for i in x:
    if m > abs(N-i):
        m = abs(N-i)
        r = i

print(r)