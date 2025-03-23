import sys


n = int(sys.stdin.readline())

h = list(sys.stdin.readline().split())

visit = [False] * 10
result = []

def bp(word, bdh, k):
    global min_val
    global max_val
    global result

    if len(word) == len(h)+1:
        result.append(''.join(map(str, word)))
        return

    for i in range(10):
        if visit[i] == True:
            continue
        
        if len(word) == 0:
            visit[i] = True
            word.append(i)
            bp(word, bdh, k)
            word.remove(i)
            visit[i] = False

        if len(word) >= 1:
            if (bdh[k] == '<' and word[-1] < i) or (bdh[k] == '>' and word[-1] > i):
                visit[i] = True
                word.append(i)
                k += 1
                bp(word, bdh, k)
                word.remove(i)
                k -= 1
                visit[i] = False

bp([], h, 0)
print(result[-1])
print(result[0])

