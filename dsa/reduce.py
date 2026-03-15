import operator
from functools import reduce
import operator
from itertools import accumulate

a = ['The', 'Leyend', 'of', 'Zelda']
r = reduce(lambda x, y: x + " " + y, a)
print(r)

a= [2, 4, 6, 8]
r= reduce(lambda x, y: x + y, a)
print(r)

a = [5, 9, 10, 32, 1, 4]
r = reduce(lambda x, y:x if x > y else y, a)
print(r)

a= [3, 3, 3]
print(reduce(operator.add, a))
print(reduce(operator.mul, a))
print(reduce(operator.add, ['What', 'the', 'fudge']))


a = [1, 2, 3, 4, 5]
res=accumulate(a, operator.add)
print(list(res))
