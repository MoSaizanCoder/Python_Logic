class Student:
    name = "karan"

s1 = Student()
print(s1.name)    

s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)    
print(car1.brand)
class Student:

    #Default constructors
    def __init__(self):
        pass

    #Parameterized constructors
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    #Function or methods
    def welcome(self):
        print("welcome student", self.name) 

    def get_marks(self):
        return self.marks       

s1 = Student("karan", 97)
print(s1.name, s1.marks)   
s1.welcome()
print(s1.get_marks())

"""Practise Question 1"""

#making class without attributes
class Student:

    #Object with Argument or attributs
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    #Function
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name, "your avg score is:", sum/3)
    
    #Static Method
    @staticmethod #decoretor
    def hello():
        print("hello")

#Calling the object and Function
s1 = Student("tony stark", [98, 97, 99])    
s1.avg()
s1.hello()


#Abstraction
"""

Hiding the implementation details of a class and only Showing the essential festures to the user.

"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")   

car1 = Car()
car1.start()

#Encapsulation
"""

Wrapping data and function into a single unit (object).

"""
#Practice Questions 2

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    #Debit
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance = ", self.final())
    
    #Credit
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance = ", self.final())
    
    #Final Balance
    def final(self):
        return self.balance

acc1 = Account(10000, 12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(5000)