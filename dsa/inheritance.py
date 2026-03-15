class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

    def sound(self, noise):
        self.noise = noise
        print(self.name, self.noise)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def deets(self):
        print(self.name, "is a", self.breed)

    def size(self):
        print(self.name, "Is Big")

class Cat(Animal):
    def size(self):
        print(self.name, "IS Small")

d = Dog("Nico", "Dalmatian")
d.info()
d.size()
d.sound("Bark")
d.deets()
c = Cat("Pyon")
c.info()
c.size()
c.sound("Miau")
