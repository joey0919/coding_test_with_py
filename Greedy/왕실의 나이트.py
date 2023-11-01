n = input()

colums = ord(n[0])
rows = int(n[1])
print(colums, rows)


step = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for i in step:
    x = colums + i[0]
    y = rows + i[1]

    if x > ord('h') or x < ord('a') or y > 8 or y < 1:
        continue
    count += 1

print(count)