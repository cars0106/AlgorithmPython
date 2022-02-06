n = int(input())
count = 0
result = 0

i = 0
while count < n:
    i += 1
    if "666" in str(i):
        count += 1
        result = i

print(result)