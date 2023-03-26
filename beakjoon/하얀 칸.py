Line = []
x = 0

for i in range(8):
    Line.append(list(input()))

for i in range(0, 8):
    for h in range(0, 8, 2):
        if Line[i][h] == "F" and i % 2 == 0:
            x += 1
    for j in range(1, 8, 2):
        if Line[i][j] == "F" and i % 2 == 1:
            x += 1
print(x)