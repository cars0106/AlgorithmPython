# 1번 문제
n = int(input())
location = list((1, 1))
process = list(map(str, input().split()))

for i in range(0, len(process)):
    if process[i] == "L":
        if location[1] - 1 != 0:
            location[1] -= 1
    elif process[i] == "R":
        if location[1] + 1 != n:
            location[1] += 1
    elif process[i] == "U":
        if location[0] - 1 != 0:
            location[0] -= 1
    elif process[i] == "D":
        if location[0] + 1 != n:
            location[0] += 1

print(location[0], location[1])

# 2번 문제
n = int(input())
time = [0, 0, 0]
count = 0

while time[0] != n + 1:
    if (str(time[0]).find("3") != -1) or (str(time[1]).find("3") != -1) or (str(time[2]).find("3") != -1):
        count += 1
    time[2] += 1
    if time[2] == 60:
        time[2] = 0
        time[1] += 1
        if time[1] == 60:
            time[1] = 0
            time[0] += 1

print(count)

# 3번 문제
coordinate = input()
location = [ord(coordinate[0]) - 96, int(coordinate[1])]
count = 0
case = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

for i in case:
    if 0 < location[0] + i[0] <= 8:
        if 0 < location[1] + i[1] <= 8:
            count += 1

print(count)

# 4번 문제
n, m = map(int, input().split())
a, b, direct = map(int, input().split())
array = [[0 for i in range(n)] for j in range(m)]
d = [[0] * m for _ in range(n)]
d[a][b] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(0, n):
    array[i] = list(map(int, input().split()))

count = 1
turn_time = 0
while True:
    direct -= 1
    if direct == -1:
        direct = 3
    nx = a + dx[direct]
    ny = b + dy[direct]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        a = nx
        b = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = a - dx[direct]
        ny = b - dy[direct]
        if array[nx][ny] == 0:
            a = nx
            b = ny
        else:
            break
        turn_time = 0

print(count)