#Solution
#Decimal to Binary using recursion
def convert(n):
    if n > 1:
        convert(n // 2)
    print(n % 2, end = '')

print ("the binary of the given number is: ")
convert(10)
