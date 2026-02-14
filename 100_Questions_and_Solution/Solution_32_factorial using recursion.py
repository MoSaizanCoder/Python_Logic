#solution
#Factorial 
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("enter a number here: "))

if n <= 0:
    print ("factorial of number less than 1 is not exist")
else:
    print("Factorial of", n, "is", fact(n))
