# 백준 1987

r, c  = map(int, (input().split()))

graph = []

for _ in range(r):
    line = input()
    graph.append(list(line))

visit = [[False for _ in range(c)] for _ in range(r)]

start = graph[0][0]


result = 0
visited_alphabets = set()

def dfs(a, b, sum, visited_alphabets):
    global result    
    
    visited_alphabets.add(graph[a][b])

    if sum > result:
        result = sum

    
    x = [0, 0, 1, -1]
    y = [-1, 1, 0, 0]

    for i in range(len(x)):
        nx = a + x[i]
        ny = b + y[i]
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if graph[nx][ny] not in visited_alphabets:
                dfs(nx, ny, sum + 1, visited_alphabets)
                
    visited_alphabets.remove(graph[a][b])         



dfs(0, 0, 1, visited_alphabets)
print(result)