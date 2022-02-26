import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap, -x)