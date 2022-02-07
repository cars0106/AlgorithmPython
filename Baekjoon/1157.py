s = input()
count = []

for i in range(26):
    count.append(0)

for i in s:
    if ord('A') <= ord(i) <= ord('Z'):
        count[ord(i) - ord('A')] += 1
    elif ord('a') <= ord(i) <= ord('z'):
        count[ord(i) - ord('a')] += 1

location = count.index(max(count))
has_same = False

for i in range(0, len(count)):
    if count[i] == max(count):
        if i != location:
            has_same = True

if has_same:
    print("?")
else:
    print(chr(location + ord('A')))