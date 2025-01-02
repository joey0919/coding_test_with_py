import sys
sys.setrecursionlimit(10**5)

m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# dp 배열: -1로 초기화 (계산되지 않음을 의미)
dp = [[-1] * n for _ in range(m)]

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def dfs(x, y):
    # 도착점에 도달하면 경로의 수는 1
    if x == n-1 and y == m-1:
        return 1

    # 이미 계산된 경로 수가 있으면 바로 반환
    if dp[y][x] != -1:
        return dp[y][x]

    # 경로의 수 초기화
    dp[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 유효 범위 내에서 내리막길로 이동 가능하면 탐색
        if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(nx, ny)

    return dp[y][x]

# (0, 0)에서 시작하여 가능한 모든 경로 탐색
print(dfs(0, 0))
