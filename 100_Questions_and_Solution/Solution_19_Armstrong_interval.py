#solution
#Armstrong in an interval

lower = int(input("enter a lower limit: "))
upper = int(input("enter a upper limit: "))

for i in range(lower,upper+1):
    order = len(str(i))
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        temp //= 10
        sum += digit ** order
    if i == sum:
        print(i)