"""
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()
"""
#Practice Questions
#Question 1

"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
"""

# Quetion 2

"""

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.dept = department
        self.salary = salary
    
    def showDetails(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
    
e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()

"""
#Question 3

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(ordr1, ordr2):
        return ordr1.price > ordr2.price

ordr1 = Order("Chips", 20)
ordr2 = Order("tea", 15)

print(ordr1 < ordr2)