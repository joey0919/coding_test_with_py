import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n = int(input().rstrip())



graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


count = [0] * (max(map(max, graph)) + 1)
def dfs(x, y, k):

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if visited[nx][ny] == False:
                if graph[nx][ny] >= k:
                    dfs(nx, ny, k)


for k in range(max(map(max, graph)) + 1):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and graph[i][j] >= k:
                count[k] += 1
                dfs(i, j, k)


count.sort(reverse=True)
print(count[0])