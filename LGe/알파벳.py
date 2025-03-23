# 깊이우선 탐색

import sys

r, c = map(int, sys.stdin.readline().split())

board = []

# board = [list(sys.stdin.readline().strip()) for _ in range(r)] # 입력받는법
board = [list(map(lambda x: ord(x)-65, input())) for _ in range(r)]
visit = [False] * 26


max_sum = 1

def dfs(x, y, s):
    global max_sum
    max_sum = max(max_sum, s)
    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # print(x, y, board[y][x])
    # print(s)
    for i in range(len(dx)):
        next_x = dx[i] + x
        next_y = dy[i] + y
        
        # 범위 확인
        if next_x >= 0 and next_x < c and next_y >=0 and next_y < r and visit[board[next_y][next_x]] == False:
            # 알파벳 검사
            visit[board[next_y][next_x]] = True
            dfs(next_x, next_y, s+1)
            visit[board[next_y][next_x]] = False
    return s

visit[board[0][0]] = True
dfs(0, 0, max_sum)
print(max_sum)