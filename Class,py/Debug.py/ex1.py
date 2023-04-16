def addTen(x):
    print("10을 더했습니다")
    return x + 10

x = [1, 2, 3, 4]

for i in range(len(x)):
    x[i] = addTen(x[i])

print(x)