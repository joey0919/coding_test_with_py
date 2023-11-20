import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

item = [0] + list(map(int, input().split()))
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            cost = min(graph[a][b], graph[a][k] + graph[k][b])
            graph[a][b] = cost

result = 0
for i in range(1, n + 1):
    line_sum = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF and graph[i][j] <= m:
            line_sum += item[j]
    if line_sum > result:
        result = line_sum
print(result)