n = input()

result = 0
for i in n:
    if ord('A') <= ord(i) <= ord('C'):
        result += 3
    elif ord('D') <= ord(i) <= ord('F'):
        result += 4
    elif ord('G') <= ord(i) <= ord('I'):
        result += 5
    elif ord('J') <= ord(i) <= ord('L'):
        result += 6
    elif ord('M') <= ord(i) <= ord('O'):
        result += 7
    elif ord('P') <= ord(i) <= ord('S'):
        result += 8
    elif ord('T') <= ord(i) <= ord('V'):
        result += 9
    elif ord('W') <= ord(i) <= ord('Z'):
        result += 9

print(result)