from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())



arr = [0] * (100000 + 1)

que = deque()
que.append(n)

def move(x):
    return [x-1, x+1, x*2]

def bfs():

    while que:
        v = que.popleft()
        if v == k:
            break;
        moving = move(v)
        for nx in moving:
            if (0 <= nx <= 100000) and arr[nx] == 0:
                que.append(nx)
                arr[nx] = arr[v] + 1



bfs()
print(arr[k])