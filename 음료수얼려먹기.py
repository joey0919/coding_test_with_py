n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(graph, x, y):

    if y >= m or y <= -1 or x <= -1 or x >= n:
        return False

    if graph[x][y] == 0:
        #이동
        graph[x][y] = 1
        dfs(graph, x-1, y)
        dfs(graph, x, y-1)
        dfs(graph, x+1, y)
        dfs(graph, x, y+1)
        return True

    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            result += 1


print(result)
