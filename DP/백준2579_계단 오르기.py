import sys
input = sys.stdin.readline
n = int(input())

arr = [0] * 301

for i in range(n):
    arr[i] = int(input())

d = [0] * 301

d[0] = arr[0]
d[1] = arr[0] + arr[1]
d[2] = max(arr[1] + arr[2], arr[0] + arr[2])

for i in range(3, n):
    d[i] = max(arr[i - 1] + d[i - 3] + arr[i], d[i - 2] + arr[i])

print(d[n - 1])