# 백트래킹: 모든 경우를 확인해야 할때

import sys

t = int(sys.stdin.readline())

for _ in range(t):

    # 11명 선수 입력
    peoples = []
    for i in range(11):
        m = list(map(int, sys.stdin.readline().split()))
        peoples.append(m)

    max_score = 0

    check = [0] * 11

    def lineup(a, score):
        global max_score

        if a == 11:
            max_score = max(score, max_score)
            return
    
        for i in range(11): # 포지션 정하기
            if check[i] or not peoples[a][i]:
                continue
            check[i] = 1
            lineup(a+1, score + peoples[a][i])
            check[i] = 0

    lineup(0, 0)
    print(max_score)
    
        
 