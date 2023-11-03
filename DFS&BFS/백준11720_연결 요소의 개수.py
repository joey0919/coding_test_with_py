n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)


visited = [False]*(n+1)
count = 0
for j in range(1, n+1):
    if visited[j] == False:
        dfs(graph, visited, j)
        count += 1


print(count)


