n = int(input())
for i in range(n):
    result = input()
    score = 0
    pre = 0
    for j in range(0, len(result)):
        if result[j] == 'O':
            score = score + 1 + pre
            pre += 1
        else:
            pre = 0
    print(score)