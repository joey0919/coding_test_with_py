import sys
input = sys.stdin.readline

n = int(input())
graph = []
INF = int(1e9)

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")

    print()