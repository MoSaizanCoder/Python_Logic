AccountBalance = 0


while True:
    User_input_operation = input("Check_Balance, Deposit, Withdraw, Exit : ")
    
    if User_input_operation == "Check_Balance":
        print(f"Your Account Balance is : {AccountBalance}")
    elif User_input_operation == "Deposit":
        Deposit = int(input("Enter Amount More Than 100 To Deposit : "))
        if Deposit >= 100:
            AccountBalance += Deposit
            print(f"Deposit Successful Total Balance : {AccountBalance}")
        else:
            print("Invalid Amount Please Enter More Than 100")
    elif User_input_operation == "Withdraw":
        Withdraw = int(input("Enter Amount More Than 100 To Withdraw : "))
        if Withdraw <= AccountBalance:
            print(f"Withdraw Successfull : {Withdraw}")
            AccountBalance -= Withdraw
            print(f"Remaining Balance : {AccountBalance}")
        else:
            print("Insufficient Balance")
    elif User_input_operation == "Exit":
        break
    else:
        print("Enter Vaild Input")