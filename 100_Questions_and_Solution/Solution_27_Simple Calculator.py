#Solution
#Simple Calculator
print("~~~~~~~~~Mini Calculator~~~~~~~")

num1 = float(input("enter a number here: "))
num2 = float(input("enter a number here: "))

print ("press + for addition \npress - for substraction \npress * for multiplication\npress / for division")

choice = input("enter your choice: ")

if choice == "+" :
    print(num1 + num2)
elif choice == "-":
    print(num1 - num2)
elif choice == "*":
    print(num1 * num2)
elif choice == "/":
    print(num1 / num2)
else:
    print("invalid choice")