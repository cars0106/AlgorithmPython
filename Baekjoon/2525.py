import sys

h, m = map(int, sys.stdin.readline().split())
r = int(sys.stdin.readline())

m += r
if m > 59:
    h += (m // 60)
    m -= (m // 60) * 60
    if h > 23:
        h -= 24

print("%d %d" % (h, m))