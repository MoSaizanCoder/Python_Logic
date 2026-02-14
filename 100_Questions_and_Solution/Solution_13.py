#Solution
#check the number is prime number or not:

num = int(input("enter a number here: "))

if num == 1:
    print("1 is neither prime nor composite")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")