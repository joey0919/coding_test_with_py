import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    num, st = input().split()
    arr.append([int(num), st])

def sort(arr):
    if(len(arr)<=1):
        return arr

    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x[0] < pivot[0]]
    right = [x for x in tail if x[0] >= pivot[0]]

    return sort(left) + [pivot] + sort(right)


for i in sort(arr):
    print(str(i[0]) + ' ' + i[1])