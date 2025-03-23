import sys

n = int(sys.stdin.readline())

m = list(map(int, sys.stdin.readline().split()))

visit = [False] * n

linked = []
max_sum = 0

def bp():
    global linked
    global max_sum

    if len(linked) == n:
        sum = 0
        for i in range(n-1):
            sum += abs(linked[i] - linked[i+1])
            
        max_sum = max(max_sum, sum)
        return
    
    for i in range(n):
        if visit[i] == False:
            visit[i] = True
            linked.append(m[i])
            bp()
            linked.pop()
            visit[i] = False


bp()
print(max_sum)




