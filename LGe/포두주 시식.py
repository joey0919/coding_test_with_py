import sys

n = int(sys.stdin.readline())

arr = []
wine = [0]*n


for _ in range(n):
    arr.append(int(sys.stdin.readline()))
    

wine[0] = arr[0]

if n > 1:
    wine[1] =  arr[0] + arr[1]

if n > 2:
    wine[2] = max(wine[1], arr[2]+arr[1], arr[2]+arr[0])

if n > 3:
    for i in range(3, n):
        wine[i] = max(wine[i-1], arr[i]+arr[i-1]+wine[i-3], arr[i]+wine[i-2])


print(wine[-1])