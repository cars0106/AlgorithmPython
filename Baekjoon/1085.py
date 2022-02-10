x, y, w, h = map(int, input().split())

array = [w - x, h - y, x, y]

print(min(array))