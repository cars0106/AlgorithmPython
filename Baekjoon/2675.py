n = int(input())
for i in range(0, n):
    t, s = map(str, input().split())
    result = ""
    for j in s:
        for k in range(0, int(t)):
            result += j
    print(result)