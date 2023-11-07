n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

start = 1
end = max(arr)
result = 0

while (start <= end):
    count = 0
    mid = (start + end) // 2

    for i in arr:
        count += i // mid
    if count < m: # 목표보다 개수가 적을 때
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

