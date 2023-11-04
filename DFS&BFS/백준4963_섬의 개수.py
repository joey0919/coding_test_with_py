import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def dfs(x, y):

    graph[x][y] = 0

    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y

        if (nx >= 0 and nx < h) and (ny < w and ny >= 0):
            if graph[nx][ny] == 1:
                dfs(nx, ny)





while True:
    w, h = map(int, input().rstrip().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().rstrip().split())) for _ in range(h)]


    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)