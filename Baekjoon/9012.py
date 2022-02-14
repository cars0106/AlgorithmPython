n = int(input())

for i in range(n):
    stack = []
    s = input()
    stoped = False
    for j in s:
        if j == "(":
            stack.append(j)
        elif j == ")" and len(stack) > 0:
            stack.pop()
        elif j == ")" and len(stack) == 0:
            stoped = True
            print("NO")
            break
    if stoped:
        continue
    else:
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")