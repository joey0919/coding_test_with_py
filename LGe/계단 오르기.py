import sys

n = int(sys.stdin.readline())

top = []

for _ in range(n):
    top.append(int(sys.stdin.readline()))

result = [0] * n

result[0] = top[0]

if n > 1:
    result[1] = top[0] + top[1]

if n > 2:
    result[2] = max(top[2] + top[1], top[2] +top[0])

for i in range(3, n):
    result[i] = max(top[i] + top[i-1] + result[i-3], top[i] + result[i-2])


print(result[-1])