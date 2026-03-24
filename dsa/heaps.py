import heapq

a = [5, 7, 9, 1, 3]

heapq.heapify(a)

print('the heap is now, ', a)

heapq.heappush(a, 4)
print('the heap is now, ', a)

smol = heapq.heappop(a)

print(f"the smallest: {smol}")
