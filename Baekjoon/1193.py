x = int(input())
n = 1
while ((n * (n + 1)) // 2) < x:
    n += 1
r = (n * (n + 1)) // 2 - x
if n % 2 == 0:
    print("%d/%d" %(n - r, 1 + r))
else:
    print("%d/%d" %(1 + r, n - r))