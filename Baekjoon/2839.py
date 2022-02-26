import sys

n = int(sys.stdin.readline())
small, big = 0, 0

while n >= 3:
    if n % 5 == 0:
        big += n // 5
        n -= 5 * (n // 5)
    else:
        n -= 3
        small += 1

if n == 0:
    print(big + small)
else:
    print("-1")