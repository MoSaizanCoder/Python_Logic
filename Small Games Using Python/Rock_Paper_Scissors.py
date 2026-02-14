import random

options = ['Rock','Paper','Scissors']
total_Round = int(input("Enter How Many Rounds You Want to Play"))

i = 1
Draw = 0
Won = 0
Lost = 0

while i <= total_Round:
    computer_choice = random.choice(options)
    user_choice = (input("Enter Your Choice Form this ['Rock','Paper','Scissors']"))

    if user_choice not in options:
        print("Enter Valid Option:", options)
    else:
        if user_choice == computer_choice:
            print(f"Made Same Choice Its Draw: {user_choice} vs {computer_choice}")
            Draw += 1
        elif user_choice == 'Rock' and computer_choice == 'Scissors':
            print(f"You Made Correct Choice You Won : {user_choice} vs {computer_choice}")
            Won += 1
        elif user_choice == 'Scissors' and computer_choice == 'Paper':
            print(f"You Made Correct Choice You Won : {user_choice} vs {computer_choice}")
            Won += 1
        elif user_choice == 'Paper' and computer_choice == 'Rock':
            print(f"You Made Correct Choice You Won : {user_choice} vs {computer_choice}")
            Won += 1
        else:
            print(f"You Made Wrong Choice You lost : {user_choice} vs {computer_choice}")
            Lost += 1
        i += 1
print("Match Ended")
print(f"Total Score: Draw = {Draw}, Won = {Won}, Lost = {Lost}")