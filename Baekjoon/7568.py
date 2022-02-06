n = int(input())
array = []
grade = []

for i in range(n):
    array.append(list(map(int, input().split())))
    grade.append(1)

for i in range(n):
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            grade[i] += 1

for i in grade:
    print(i, end=" ")