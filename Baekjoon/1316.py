n = int(input())

count = 0
for r in range(n):
    s = input()
    array = []
    is_sequence = True

    for i in s:
        if len(array) == 0:
            array.append(i)
        else:
            new_count = 0
            for j in range(len(array)):
                if i == array[j]:
                    if j == len(array) - 1:
                        continue
                    else:
                        is_sequence = False
                        break
                else:
                    new_count += 1
            if new_count == len(array):
                array.append(i)
    if is_sequence:
        count += 1

print(count)