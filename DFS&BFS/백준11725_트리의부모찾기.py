import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1)

for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            result[i] = v
            dfs(i)


dfs(1)

for i in range(2, (n+1)):
    print(result[i])