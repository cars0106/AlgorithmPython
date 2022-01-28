n = int(input())
grade = list(map(int, input().split()))

m = max(grade)
sum = 0
for i in range(0, len(grade)):
    grade[i] = grade[i] / m * 100
    sum += grade[i]

print("%.2f" %(sum / n))