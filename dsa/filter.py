# the filter function is used to extract elements from an iterable
# list, tuple or set

def startsA(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(startsA, li)
print(list(res))

# syntax filter(function, iterable)
