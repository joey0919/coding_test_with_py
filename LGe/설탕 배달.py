import sys

n = int(sys.stdin.readline())

min_result = n

for i in range(0, n//5+1):
    remain = n-(5*i)
    if remain%3 == 0: # 3으로 나누어 떨어짐
        min_result = min(min_result, i+remain//3)


if min_result == n:
    print("-1")
else:
    print(min_result)