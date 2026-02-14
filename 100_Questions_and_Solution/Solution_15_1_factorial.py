#Solution
#find the factorial of a number

num = int(input("enter a number: "))

factorial = 1

if num < 0 :
    print("factorial does not exist for negative numbers")
if num == 0 :
    print("factorial of 0 is 1")
if num > 0 :
    for i in range(1, num + 1):
        factorial = factorial * i
    print("factorial of", num, "is", factorial)
