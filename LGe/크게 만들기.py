import sys
import collections

n, k = map(int, sys.stdin.readline().split())

num = int(input())

# 숫자 list로 만들기
line = list(map(str, str(num)))

stack = []


for i in line:
    while (stack and k>0 and stack[-1] < i):
        stack.pop()
        k -= 1

    stack.append(i)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))