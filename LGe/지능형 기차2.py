import sys


remain = 0
max_remain = 0

for i in range(10):

    t_out, t_in = map(int, sys.stdin.readline().split())

    remain -= t_out
    remain += t_in

    max_remain = max(remain, max_remain)


print(max_remain)
