import sys
input = sys.stdin.readline
n = int(input())

d = [1] * 1000
arr = list(map(int, input().split()))

for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            d[i] = max(d[j] + 1, d[i])

print(max(d))