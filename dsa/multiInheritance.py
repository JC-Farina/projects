class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def showRole(self):
        print(self.name, "is an employee")

    def deets(self):
        print(self.name, "earns", self.salary)

class Manager(Employee):
    def department(self, dept):
        print(self.name, "manages", dept, 
              "department")

class Intern(Person):
    def role(self):
        print(self.name, "is a intern")

mgr= Manager("Randy", 75000)
mgr.deets()
mgr.showRole()
mgr.department("HR")

emp = Employee("Paul", 45000)
emp.deets()
emp.showRole()

tern = Intern("Joel")
tern.role()
