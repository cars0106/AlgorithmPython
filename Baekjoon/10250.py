n = int(input())
for i in range(n):
    data = list(map(int, input().split()))

    room = data[2] // data[0] + 1
    floor = data[2] % data[0]

    if floor == 0:
        room = data[2] // data[0]
        floor = data[0]

    print("%d" % (floor * 100 + room))