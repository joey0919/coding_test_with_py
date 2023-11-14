n, m = map(int, input().split())

coin = [int(input()) for _ in range(n)]
coin.sort()

d = [10001] * (m+1)
d[0] = 0

for i in range(1, len(coin)):
    for j in range(1, m+1):
        if d[j - coin[i]] != 10001:
            d[j] = min(d[j - coin[i]] + 1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
