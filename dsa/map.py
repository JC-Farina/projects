def double(val):
    return val * 2

a = [1, 2, 3, 4]
res = list(map(double, a))
print(res)

print(list(map(lambda x: x ** 2, a)))

b =[5, 6, 7, 8]
res = list(map(lambda x, y: x + y, a, b))
print(res)


fruut = ['apple', 'pear', 'peaches', 'watermelon']
res = map(str.upper, fruut)
print(list(res))

res = map(lambda s: s[0], fruut)
print(list(res))

s = ['   hello   ', 'there           ', '        Kennobi']
res = map(str.strip, s)
print(list(res))

cels = [0, 20, 37, 100]
faren = map(lambda x: (x * 9/5) + 32, cels)
print(list(faren))
