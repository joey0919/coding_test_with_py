n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]

result = 0

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur = arr[0]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                count += 1
                cur = arr[i]

        if count >= m:
            global result
            result = mid
            start = mid + 1
        else:
            end = mid - 1


binary_search(arr, start, end)
print(result)

