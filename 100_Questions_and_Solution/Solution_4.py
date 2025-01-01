#python program to solve Quadratic Equation
#a, b and c are real numbers
# a!=0
# formula ax**2 + bx + c 

import cmath

a =int(input("enter number (a!=0): "))
b =int(input("enter number: "))
c =int(input("enter number: "))

#formula for discriminant
d = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print("the roots are" , root1 , "and" , root2)