li = [10, 20, 30, 40]
li2 = ['apple', 'tomato', 'cherry']
li3 = list(('Fester', 10, True, 3.14))
print(li)
print(li2)
print(li3)

li4 = [2] * 5
li5 = [0] * 3
print(li4, li5)

li5 = ['a','b','c','d']
print(li5[0])
print(li5[-1])
print(li5[1:3])

a = []

a.append(10)
print(a)

a.append(20)
print(f"append{a}")

a.extend([30,40,50])
print(f"extend{a}")

a[1] = 50
print(f"updating index 1{a}")

a.remove(50)
print(f"after remove{a}")

pval = a.pop(1)
print(f"popped val {pval}, after pop {a}")

del a[0]
print(f"after del{a}")

a.clear()
print(f"clear{a}")

a = ['apple', 'orange', 'pear', 'grape']

for fruit in a:
    print(fruit)

matrix = [ [1, 4, 7]
                                ]
