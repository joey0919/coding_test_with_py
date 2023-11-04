import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
#첫째 줄 N
n = int(input().rstrip())

graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def dfs(x, y):

    visited[x][y] = True
    pre = graph[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0<= ny < n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == pre:
                    dfs(nx, ny)



count = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            count += 1
            dfs(i, j)


for a in range(n):
    for b in range(n):
        if graph[a][b] == 'G':
            graph[a][b] = 'R'

count2 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            count2 += 1

print(count, count2)