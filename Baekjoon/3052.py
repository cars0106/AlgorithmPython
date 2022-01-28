array = []
for i in range(0, 10):
    array.append(int(input()) % 42)

for i in range(0, 10):
    for j in range(i + 1, 10):
        if array[i] == array[j]:
            array[i] = -1

count = 0
for i in range(0, 10):
    if array[i] != -1:
        count += 1

print(count)

# 더 간단한 방법
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))