import sys
import heapq

input = sys.stdin.readline

n = int(input())  # 도시 수
m = int(input())  # 버스 수

road = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    road[u].append((v, w))

start_city, end_city = map(int, input().split())

# 최소 비용 테이블
result = [float('inf')] * (n + 1)
# 이전 도시 기록
prev_node = [0] * (n + 1)

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    result[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if result[now] < dist:
            continue

        for next_city, cost in road[now]:
            total = dist + cost
            if total < result[next_city]:
                result[next_city] = total
                prev_node[next_city] = now
                heapq.heappush(heap, (total, next_city))

dijkstra(start_city)

# 경로 역추적
path = []
now = end_city
while now:
    path.append(now)
    now = prev_node[now]
path.reverse()

# 출력
print(result[end_city])       # 최소 비용
print(len(path))              # 도시 개수
print(' '.join(map(str, path)))  # 경로
