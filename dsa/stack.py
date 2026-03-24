stack = []

stack.append('g')
stack.append('g')
stack.append('6')
stack.append('9')

print('Initial stack')
print(stack)

p1 =stack.pop()
p2 = stack.pop()
p3 = stack.pop()
p4 = stack.pop()

print(f"popped nums are, {p1}, {p2}, {p3}, {p4}")
print('The stack is now: ')
print(stack)
