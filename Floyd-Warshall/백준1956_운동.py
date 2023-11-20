import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c



for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            result = min(result, graph[i][j])


if result == INF:
    print(-1)
else:
    print(result)