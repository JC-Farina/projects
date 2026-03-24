queue = []

queue.append('w')
queue.append('t')
queue.append('f')

print('initial queue: ')
print(queue)

qp0 = queue.pop(0)
qp1 = queue.pop(0)
qp2 = queue.pop(0)

print(f"dequed elements: {qp0}, {qp1}, {qp2}")
print(queue)
