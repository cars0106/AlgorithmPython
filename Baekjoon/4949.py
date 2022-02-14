while True:
    s = input()
    if s == ".":
        break
    else:
        stack = []
        is_no = False
        for i in s:
            if i == "(":
                stack.append("(")
            elif i == "[":
                stack.append("[")
            elif i == ")":
                if len(stack) != 0 and stack.pop() == "(":
                    continue
                else:
                    is_no = True
                    print("no")
                    break
            elif i == "]":
                if len(stack) != 0 and stack.pop() == "[":
                    continue
                else:
                    is_no = True
                    print("no")
                    break
        if is_no:
            continue
        else:
            if len(stack) == 0:
                print("yes")
            else:
                print("no")