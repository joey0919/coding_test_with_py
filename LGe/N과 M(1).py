import sys

n, m = map(int, sys.stdin.readline().split())

rrr = []
visit = [0] * n

def rec():
    if len(rrr) == m:
        print(' '.join(map(str, rrr)))
        return

    for i in range(1, n+1):
        if i not in rrr:
            rrr.append(i)
            rec()
            rrr.pop()


rec()