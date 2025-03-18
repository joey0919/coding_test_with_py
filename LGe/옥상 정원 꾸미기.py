import sys

n = int(sys.stdin.readline())

bld = []

for _ in range(n):
    high = int(sys.stdin.readline())
    bld.append(high)




stack = []
cnt = 0

for h in bld:
    while stack and stack[-1] <= h:
        stack.pop()

    stack.append(h)
    cnt += len(stack)-1


print(cnt)