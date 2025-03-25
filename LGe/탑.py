import sys

n = int(sys.stdin.readline())

tops = list(map(int, sys.stdin.readline().split()))
tops.reverse()

stack = []
result = [0] * n
for i in range(len(tops)):
    while stack and stack[-1][0] < tops[i]:
        top, seq = stack.pop()
        result[seq] = n-i
    stack.append((tops[i], i))
    
result.reverse()
print(' '.join(map(str, result)))

