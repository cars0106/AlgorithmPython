# 1번 문제
number = int(input())
summ = 0
if number >= 500:
    summ += int(number / 500)
    number -= (500 * int(number / 500))
if number >= 100:
    summ += int(number / 100)
    number -= (100 * int(number / 100))
if number >= 50:
    summ += int(number / 50)
    number -= (50 * int(number / 50))
if number >= 10:
    summ += int(number / 10)
    number -= (10 * int(number / 10))
print(summ)

# 2번 문제
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse=True)
maximum = array[0]
minimax = array[1]
result = 0
count = 0

for i in range(0, m):
    if count == k:
        result += minimax
        count = 0
    else:
        result += maximum
        count += 1

print(result)

# 3번 문제
n, m = map(int, input().split())
minimum = 0

for i in range(0, n):
    array = list(map(int, input().split()))
    if minimum < min(array):
        minimum = min(array)

print(minimum)

# 4번 문제
n, k = map(int, input().split())
result = 0

while n != 1:
    if (n % k) == 0:
        n = n / k
        result += 1
    else:
        n = n - 1
        result += 1

print(result)