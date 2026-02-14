#Solution
#Sum of natural number using Recursion

def naturalsum (n):
    if n <= 1:
        return n
    else:
        return n + naturalsum(n-1)
n = int(input("enter a number: "))
if n<=0:
    print("Please enter a positive integer")
else:
    print(naturalsum(n))