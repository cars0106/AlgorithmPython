import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    queue.append(i + 1)

while len(queue) > 1:
    queue.rotate(-1)
    queue.pop()
    queue.rotate(-1)

print(queue[0])