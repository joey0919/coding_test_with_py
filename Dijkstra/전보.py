import sys
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())

INF = int(1e9)
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
print(graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 처음 값 넣기
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
dijkstra(c)
count = 0
resultd = 0
for i in range(len(distance)):
    if distance[i] != int(1e9) and distance[i] != 0:
        if resultd < distance[i]:
            resultd = distance[i]
        count += 1

print(count, resultd)