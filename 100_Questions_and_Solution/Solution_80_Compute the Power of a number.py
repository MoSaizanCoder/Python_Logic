#Solution 1 Using While loop

base = int(input("Enter the base number: "))
exponent = int(input("Enter the base number: "))

result = 1
while exponent != 0:
    result *= base
    exponent -= 1
    print(result)

#Solution 2 Using For Loop

base = int(input("Enter the base number: "))
exponent = int(input("Enter the base number: "))

result = 1
for i in range(exponent):
    result *= base
print(result)

#Solution 3 Using Power() Function

base = int(input("Enter the base number: "))
exponent = int(input("Enter the base number: "))

x = pow(base,exponent)
print(x)

#Solution 4 Using Exponentiation Operator

base = 2 
exponent = 3

value = base**exponent
print(value)