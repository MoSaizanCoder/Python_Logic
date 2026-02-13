import random
correct_int = random.randint(1,100)

i = 1
while i <= 10:
    Enter_num = int(input("Enter Your Guess"))
    if Enter_num == correct_int:
        print("Your Guess is Correcct :",Enter_num)
        break
    elif Enter_num < correct_int:
        print("Your Guess is Too Small :",Enter_num)
    else:
        print("Your Guess is Too Big :",Enter_num)

    i+=1
if i > 10:
    print("Game Over! The correct number was:", correct_int)