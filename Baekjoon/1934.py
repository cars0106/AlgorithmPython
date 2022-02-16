def gcd(num1, num2):
    num_a, num_b = num1, num2
    n = 0

    while num_b != 0:
        n = num_a % num_b
        num_a = num_b
        num_b = n

    return num_a


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a

    if a == 1:
        print(a * b)
    else:
        g = gcd(a, b)
        print(g * (a // g) * (b // g))