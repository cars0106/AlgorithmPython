import sys

a, b, v = map(int, sys.stdin.readline().split())
k = (v - b) / (a - b)

if int(k) == k:
    k = int(k)
else:
    k = int(k) + 1

print(k)