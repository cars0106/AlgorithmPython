n = int(input())
result = 0

for i in range(1, n):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        result = i
        break

print(result)