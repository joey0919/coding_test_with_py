import sys
sys.setrecursionlimit(10**5)

def dfs(graph, v, visited, group):
    visited[v] = group

    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(graph, i, visited, -group):
                return False
        elif visited[i] == group:
            return False
        
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (v+1)

    result = True

    for i in range(1, v + 1):
        if visited[i] == 0:
            if not dfs(graph, i, visited, 1):
                result = False
                break

    print("YES" if result else "NO")

