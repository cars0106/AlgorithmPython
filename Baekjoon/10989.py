import sys

n = int(sys.stdin.readline())
counting_array = []
for i in range(10001):
    counting_array.append(0)

for i in range(n):
    tmp = int(sys.stdin.readline())
    counting_array[tmp] += 1

for i in range(10001):
    if counting_array[i] != 0:
        for j in range(counting_array[i]):
            print(i)