n = int(input())
array = list(map(int, input().split()))
result = 0

for i in array:
    if i != 1:
        check = 0
        for j in range(2, i):
            if i % j == 0:
                check += 1
        if check == 0:
            result += 1

print(result)