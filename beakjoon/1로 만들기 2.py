n = int(input())

mins = [0] * (n + 1)
routes = [[]] * (n + 1)

mins[1] = 0
routes[1] = [1]

for i in range(2, n + 1):
    mins[i] = mins[i - 1] + 1
    routes[i] = [i] + routes[i - 1]

    if i % 2 == 0 and mins[i] > mins[i // 2] + 1:
        mins[i] = mins[i // 2] + 1
        routes[i] = [i] + routes[i // 2]
    
    if i % 3 == 0 and mins[i] > mins[i // 3] + 1:
        mins[i] = mins[i // 3] + 1
        routes[i] = [i] + routes[i // 3]

print(mins[n])
print(*routes[n])