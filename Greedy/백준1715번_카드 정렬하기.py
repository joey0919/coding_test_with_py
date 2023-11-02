from heapq import heappush, heappop
#입력
n = int(input())

heap = []


for key in range(n):
    num = int(input())
    heappush(heap, num)

result = 0

for i in range(n-1):
    cur = heappop(heap)
    nex = heappop(heap)
    result += cur+nex
    heappush(heap, cur+nex)

print(result)
# heapq가 PriorityQueue 클래스를 사용하는것 보다 빠르다