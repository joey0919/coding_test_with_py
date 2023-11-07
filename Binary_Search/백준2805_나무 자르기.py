n, m = map(int, input().split())

arr = list(map(int, input().split()))
start = 1
end = max(arr)
result = 0

while(start <= end):
    length = 0
    mid = (start + end) // 2

    for i in arr:
        if i - mid > 0:
            length += (i - mid)
    if length < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)