import sys
input = sys.stdin.readline

#입력
n = int(input())

#수열
matrix = [int(input()) for _ in range(n)]


plus = list(filter(lambda x:x > 1, matrix)) #양수
minus = list(filter(lambda x:x <= 0, matrix)) #음수
plus.sort(reverse=True)
minus.sort()

result = sum(list(filter(lambda x:x == 1, matrix)))

#양수 계산
for i in range(0, len(plus), 2):
    if (i + 1) >= (len(plus)): # i+1이 범위를 벗어날 때
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]

#음수 계산
for i in range(0, len(minus), 2):
    if (i+1) >= (len(minus)):
        result += minus[i]
    else:
        result += minus[i] * minus[i + 1]



print(result)