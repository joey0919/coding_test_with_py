import sys



while True:
    line = sys.stdin.readline().rstrip()
    
    if line == '.':
        break

    line = list(line)
    stack = []

    cnt = 0
    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        if i == ")" or i == "]":
            if stack and ((stack[-1] == "(" and i == ")") or (stack[-1] == "[" and i == "]")):
                stack.pop()
            else:
                cnt += 1


    if len(stack) == 0 and cnt == 0:
        print("yes")
    else:
        print("no")
        