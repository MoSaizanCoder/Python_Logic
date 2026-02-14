import random #importing Random

curr_position = 0

snakes = {98: 20, 75: 10, 50: 5, 78: 68, 35:20}  #Snakes
ladders = {4: 40, 15: 55, 30: 80, 60:72, 54:74} #Ladders

print("--- START GAME ---")
print("Rule: 0 se nikalne ke liye 6 chahiye!")

while True:
    user_in = input("Enter 'Y' or 'y' to role the dice : ") #User Input
    if user_in == "Y" or user_in == "y": 
        dice_role = random.randint(1,6) #Dice Role
        print(f"Dice Role is : {dice_role}")

        # Game Start Logic If Current Position 0.
        if curr_position == 0:
            if dice_role == 6:
                curr_position = 1
                print("🚀 You started! Moved to position 1.")
            else:
                print("🔒 Need a 6 to start. Try again.")

        # Main Movement Logic Starts.
        else:
            if curr_position + dice_role <= 100: # If Current Position is less than equal 100 then move.
                curr_position += dice_role # Updating Current Position

                # Snakes Bite logic.
                if curr_position in snakes:
                    print(f"🐍 Oh no! Snake at {curr_position} bit you!")
                    curr_position = snakes[curr_position]
                    print(f"🔻 Fell down to {curr_position}")
                
                # Ladder Climbing Logic.
                elif curr_position in ladders:
                    print(f"🪜 Wow! Ladder at {curr_position}!")
                    curr_position = ladders[curr_position]
                    print(f"🔼 Climbed up to {curr_position}")
                
                # Normal Movement Message.
                else:
                    print(f"✅ Moved forward.")

            # More than 100 handling with Message.
            else:
                print("🚫 Move not possible! You need exact number.")

        print(f"Current Position : {curr_position}") # Printing Current Position.

        # Winning Logic if Current position is 100.
        if curr_position == 100:
            print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
            break

    # Handling Invalid Input from User.
    else:
        print("Exiting Game Invalid Input")
        break