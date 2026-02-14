#Solution 1 Using While loop

num = int(input("Enter a number here: "))

i = 0
while num != 0:
    digit = num%10
    i = i*10 + digit
    num = num//10

print(i)

#Solution 2 Using string Slicing

num = int(input("enter a number here: "))
print(str(num)[::-1])