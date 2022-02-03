s = input()
count = 0

for i in range(0, len(s)):
    if i < len(s) - 1:
        if s[i] == 'c':
            if s[i + 1] == '=' or s[i + 1] == '-':
                continue
            else:
                count += 1
        elif s[i] == 'd':
            if s[i + 1] == '-':
                continue
            elif i < len(s) - 2 and s[i + 1] == 'z' and s[i + 2] == '=':
                continue
            else:
                count += 1
        elif s[i] == 'l':
            if s[i + 1] == 'j':
                continue
            else:
                count += 1
        elif s[i] == 'n':
            if s[i + 1] == 'j':
                continue
            else:
                count += 1
        elif s[i] == 's':
            if s[i + 1] == '=':
                continue
            else:
                count += 1
        elif s[i] == 'z':
            if s[i + 1] == '=':
                continue
            else:
                count += 1
        else:
            count += 1
    else:
        count += 1

print(count)