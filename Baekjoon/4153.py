while True:
    array = list(map(int, input().split()))
    if array[0] == 0 and array[1] == 0 and array[2] == 0:
        break
    else:
        array.sort()
        if array[0] * array[0] + array[1] * array[1] == array[2] * array[2]:
            print("right")
        else:
            print("wrong")