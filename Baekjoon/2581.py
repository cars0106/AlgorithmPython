def check(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


n = int(input())
m = int(input())
array = []

for i in range(n, m + 1):
    if check(i):
        array.append(i)

if len(array) >= 1:
    print(sum(array))
    print(array[0])
else:
    print(-1)