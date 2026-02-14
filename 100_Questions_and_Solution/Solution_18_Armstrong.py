#Solution
#Armstrong
num = int(input("enter a number: "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum+digit**order
    temp = temp // 10


if sum == num :
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
