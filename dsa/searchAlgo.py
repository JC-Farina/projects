from bisect import bisect
import bisect

a = [2, 4, 6, 8, 10]

# linear search with the in operator
print(6 in a)

# linear search using count module
print(a.count(7) > 0)

pos = bisect.bisect_left(a, 8)
print("found at index", pos)
