import sys

sys.setrecursionlimit(10**4)

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def melt():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    melted = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                melt_count = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                        melt_count += 1
                melted[i][j] = melt_count

    for i in range(n):
        for j in range(m):
            graph[i][j] -= melted[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

def dfs(x, y):
    # 방문 처리
    visit[y][x] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 인접한 빙산 탐색
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n:
            if not visit[ny][nx] and graph[ny][nx] > 0:
                dfs(nx, ny)

def count_icebergs():
    # 덩어리 수 계산
    global visit
    visit = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visit[i][j]:
                dfs(j, i)
                count += 1

    return count

year = 0
while True:
    # 덩어리 계산
    iceberg_count = count_icebergs()

    # 종료 조건
    if iceberg_count == 0:
        print(0)
        break
    if iceberg_count >= 2:
        print(year)
        break

    # 빙산 녹이기
    melt()
    year += 1
