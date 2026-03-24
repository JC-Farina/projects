# compile time polymorphism

class Calculator:
    def mult(self, a=1, b=1, *args):
        res = a * b
        for num in args:
            res *= num
        return res

calc = Calculator()

print(calc.mult())
print(calc.mult(4))
print(calc.mult(2, 3))
print(calc.mult(2, 3, 4))

class Animal:
    def sound(self):
        return "Animal noises"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Miau"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())

class Pen:
    def use(self):
        return "writing"

class Eraser:
    def use(self):
        return "Erasing"

def performTask(tool):
    print(tool.use())

performTask(Pen())
performTask(Eraser())
