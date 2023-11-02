from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

count = 0
#상하좌우
loc = [(1, 0), (-1, 0), (0, -1), (0, 1)]

deque = deque()

def bfs(x, y):

    if x == 1 and y == 1:
        deque.append((x-1, y-1))
        #graph[x-1][y-1] = 0
        print(f'({x},{y})', end=' ')

    while deque:
        v = deque.popleft()
        for k in loc:
            if v[0] + k[0] >= n or v[0] + k[0] <= -1 or v[1] + k[1] >= m or v[0] + k[0] <= -1:
                continue
            if graph[v[0] + k[0]][v[1] + k[1]] == 1:
                deque.append((v[0] + k[0], v[1] + k[1]))
                print(f'({v[0] + k[0] + 1},{v[1] + k[1] + 1})', end=' ')

                graph[v[0] + k[0]][v[1] + k[1]] = graph[v[0]][v[1]] + 1

    return graph[n-1][m-1]

print(bfs(1, 1))