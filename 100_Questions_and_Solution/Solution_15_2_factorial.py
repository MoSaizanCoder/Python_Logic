#Solution
#Recursion


def fact(a):
    if a ==0:
        return 1
    else:
        return ((a)*fact(a-1))

num = int(input("enter a number: "))

result = fact(num)
print("Factorial of",num,"is",result)
