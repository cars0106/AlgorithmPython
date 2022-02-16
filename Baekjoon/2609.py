# 방법1
array = list(map(int, input().split()))
g = 0
array.sort()

for i in range(1, array[0] + 1):
    if array[0] % i == 0 and array[1] % i == 0:
        g = i

l = g * (array[0] // g) * (array[1] // g)

print(g, l)

# 방법 2
n, m = map(int, input().split())
g = 0

if n < m:
    for i in range(1, n + 1):
        if n % i == 0 and m % i == 0:
            g = i
else:
    for i in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            g = i

l = g * (n // g) * (m // g)

print(g, l)