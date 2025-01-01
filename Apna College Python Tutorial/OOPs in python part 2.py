"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass) #private
        #print(self.acc_pass) #public

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())
"""

#class Person:
#    __name = "anonymous"
#
#    def __hello(self, name):
#        print("hello person!")
#    def welcome(self):
#        self.__hello(self)
#
#p1 = Person()
#print(p1.welcome())

#Inheritance Single and Multi-Level

"""

class Car:
    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stoped..")

class Toyota_cars(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota_cars):
    def __init__(self, type):
        self.type = type    

car1 = Fortuner("diesel")
car1.start()

"""

#Multiple Inheritance

"""

class A:
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"
class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

"""

#Super Method In Inheritance

"""

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")
    @staticmethod
    def stop():
        print("Car stopped..")

class Toyota_cars(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = Toyota_cars("prius","electric")
print(car1.type)

"""

#class method 

"""

class Person:
    name = "anonymous"

    #def ChangeName(self, name):
        #Person.name = name
        #self.__class__.name = " Rahul Kumar"

    @classmethod  #Class Decorator
    def ChangeName(cls, name):
        cls.name = name

p1 = Person()
p1.ChangeName("rahul kumar")
print(p1.name)
print(Person.name)

"""
"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
    
    #def calcPercentage(self):
    #    self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)

"""

