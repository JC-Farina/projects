# Decorators are flexible ways to modify or extend behavior of functions or methods
# without changing their actual code(Hardcodding)
# Some uses of this are: Logging (track function calls), Authentication (restrict web app access)
# Caching (store results using functools.lru_cache), Retry logic (automatically retry failed network calls)


def decorator(func):
    def wrapper():
        print("not decorated")
        func()
        print("decorated! S P A R K L E")
    return wrapper


@decorator # using decorator func
def greet():
    print("Hello World!!")

greet()

# decorator with parameters

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print('Before executioin')
        result = func(*args, **kwargs)
        print('After execution')
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(6, 9))

# setting variable as a function

def greeting(n):
    return f"Hello {n}"

sayHi = greeting

print(sayHi("Fari"))

# function as argument 
# f = function
# v = argument
def apply(f, v):
    return f(v)

res = apply(sayHi, 'Puter')
print(res)

# funtion from function

def makeMult(f):
    def mult(x):
        return x * f
    return mult
dbl = makeMult(2)
print(dbl(5))

# higher order function

def vfun(f, x):
    return f(x)

def square(x):
    return x * x

res = vfun(square, 5)
print(res)

def simpleDecorator(funk):
    def wrapper():
        print("starting func...")
        funk()
        print("... ending func")
    return wrapper

@simpleDecorator
def gret():
    print("am here")
gret()

# Method decoration

def methodDecorator(fu):
    def wrapper (self, *args, **kwargs):
        print("executing decorator")
        rest = fu(self, *args, **kwargs)
        print("decoration executed")
        return rest
    return wrapper

class Myclass:
    @methodDecorator
    def sayHello(self):
        print("Hello")
obj = Myclass()
obj.sayHello()

#class decorator


def funky(cls):
    cls.className = cls.__name__
    return cls

@funky
class Person:
    pass
print(Person.className)

# built in operators
# @staticmethod : defines a method that does NOT operate on a class instance
# usefull for adding methods without creating instances

class Mathops:
    @staticmethod
    def addition(x, y):
        return x + y
res = Mathops.addition(6, 9)
print(res)

# @classmethod : defines method that operates on the class itself
# usefull for modifying a class state across multiple instances

class Employee:
    raiseAmount = float = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

print(Employee.raiseAmount)
Employee.setRaiseAmount(1.10)
print(Employee.raiseAmount)

# @property : used to define a method as a property, allowing attribute-like access

class Circle:
    def __init__(self, radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius can NOT be a negative number")

    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

c = Circle(5)
print(f"radius = {c.radius}, area = {c.area}")
c.radius = 10
print(f"radius = {c.radius}, area = {c.area}")

# Chaining Decorators
# multiple decorators con be applied to the same function
# this works in sequence to add layered behavior

def dec1(funkf):
    def inner():
        x = funkf()
        return x * x
    return inner

def dec2(funkf):
    def inner():
        x = funkf()
        return 2 * x
    return inner

@dec1
@dec2
def num():
    return 10

@dec1
@dec2
def num2():
    return 10

print( num(), num2())
