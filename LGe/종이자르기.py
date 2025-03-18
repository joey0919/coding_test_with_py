import sys

n, m = map(int, sys.stdin.readline().split())
iter = int(sys.stdin.readline())

garo = []
sero = []

for _ in range(iter):
    a, b = map(int, sys.stdin.readline().split())

    if a == 0:  # 가로
        garo.append(b)
    if a == 1: # 세로
        sero.append(b)


garo.append(0)
garo.append(m)
sero.append(0)
sero.append(n)

garo.sort()
sero.sort()

garo_max = 0
sero_max = 0

garo_gan = []
sero_gan = []


for i in range(1, len(garo)):
    garo_gan.append(garo[i]-garo[i-1])

for i in range(1, len(sero)):
    sero_gan.append(sero[i]-sero[i-1])


print(max(garo_gan)*max(sero_gan))