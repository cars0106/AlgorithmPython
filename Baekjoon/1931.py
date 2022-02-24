import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

array = sorted(array, key=lambda a: a[0])
array = sorted(array, key=lambda a: a[1])

last = 0
count = 0
for i, j in array:
    if i >= last:
        count += 1
        last = j

print(count)