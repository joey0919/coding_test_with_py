# 우선순위 큐 - Heap 사용
import sys
import heapq

n = int(sys.stdin.readline())

time = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    time.append([s, t])

time.sort(key=lambda x: (x[0], x[1]))

heap = [time[0][1]]

for i in range(1, n):
    if heap[0] <= time[i][0]: # 끝나는 시간이 시작 시간보다 같거나 작음
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))