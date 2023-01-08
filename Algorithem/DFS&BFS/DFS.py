N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

visited = [0] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

def dfs(V):
    visited[V] = 1
    for i in range(N+1):
        if graph[V][i] == 1 and not visited[i]:
            dfs(i)