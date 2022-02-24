n, k = map(int, input().split())
array = []

for i in range(n):
    array.append(int(input()))

result = 0
for i in range(n):
    if k // array[n - i - 1] != 0:
        result += (k // array[len(array) - i - 1])
        k -= (k // array[len(array) - i - 1]) * array[len(array) - i - 1]

print(result)