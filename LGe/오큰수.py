import sys

n = int(sys.stdin.readline())


sy = list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1] * n

for i in range(len(sy)):
    while stack and stack[-1][1] < sy[i]:
        # print(sy[i], stack)
        a, b = stack.pop()
        result[a] = sy[i]


    stack.append((i, sy[i]))


print(' '.join(map(str, result)))