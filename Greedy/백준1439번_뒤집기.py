s = input()
cnt = 0
prev='?'

for i in s:
    if i != prev:
        prev=i
        cnt += 1

print((cnt)//2)

# 내 풀이와 달랐던 점
# 1인경우 0인경우 모두 세서 문제를 풀었다. 하지만 그냥 전체 등분수/2를 하면 결과 값이 나온다..