import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

def bfs():
    # 익은 토마토 들어옴
    while queue:
        (a, b) = queue.popleft()

        for i in range(4): #익은토마토 상하좌우 익게하기
            nx = a + dx[i]
            ny = b + dy[i]
            if (0 <= ny < n) and (0 <= nx < m):
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[a][b] + 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))


bfs()

res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    res = max(res, max(i))

print(res-1)