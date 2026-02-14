import random #importing Random
import time #importing Time


snakes = {98: 20, 75: 10, 50: 5, 78: 68, 35:20}  #Snakes
ladders = {4: 40, 15: 55, 30: 80, 60:72, 54:74} #Ladders

print("--- Multiplayer Ludo GAME Started ---")
print("Rule: 0 se nikalne ke liye 6 chahiye!")

while True:
    try:
        total_Players = int(input("Enter Number of Players 2-4 : "))
        if 2 <= total_Players <= 4:
            break
        print("Please Enter Valid Number between 2-4")
    
    except ValueError:
        print("Invalid Input Number Only")

while True:
    try:
        computers = int(input(f"Enter how many Computer Player you want 0 - {total_Players - 1} : "))
        if 0 <= computers < total_Players:
            break
        print(f"Enter Valid number between 0 - {total_Players-1}")
    except ValueError:
        print("Enter Valid Input Number Only")

Players_list = []

humans = total_Players - computers

for i in range(humans):
    Players_list.append({"name": input("Enter Player_Name"), "curr_position": 0, "is_bot": False})

for i in range(computers):
    Players_list.append({"name": f"Computer {i+1}", "curr_position": 0, "is_bot": True})

print("\nGame Started! Participants:", [p['name'] for p in Players_list])
print("-" * 40)

Game_Over = False

while not Game_Over:
    for p in Players_list:
        if not p['is_bot']:
            user_in = input("Enter 'Y' or 'y' to role the dice : ") #User Input
            if user_in == "Y" or user_in == "y": 
                dice_role = random.randint(1,6) #Dice Role
                print(f"{p['name']} Dice Role is : {dice_role}")
            # Handling Invalid Input from User.
            else:
                print("Exiting Game Invalid Input")
                break
        else:
            print(f"{p['name']}   Thinking...", end="", flush=True)
            time.sleep(1) # 1 second ka delay
            print(" Rolling!")

            # Dice Roll
            dice_role = random.randint(1, 6)
            print(f"{p['name']}  🎲 Rolled a {dice_role}")

        # Game Start Logic If Current Position 0.
        if p['curr_position'] == 0:
            if dice_role == 6:
                p['curr_position'] = 1
                print(f"🚀 {p['name']} started! Moved to position 1.")
            else:
                print(f" {p['name']} 🔒 Need a 6 to start. Try again.")

        # Main Movement Logic Starts.
        else:
            if p['curr_position'] + dice_role <= 100: # If Current Position is less than equal 100 then move.
                p['curr_position'] += dice_role # Updating Current Position

                # Snakes Bite logic.
                if p['curr_position'] in snakes:
                    print(f"🐍 Oh no! Snake at {p['curr_position']} bit you!")
                    p['curr_position'] = snakes[p['curr_position']]
                    print(f"{p['name']} 🔻 Fell down to {p['curr_position']}")
                
                # Ladder Climbing Logic.
                elif p['curr_position'] in ladders:
                    print(f"🪜 Wow! Ladder at {p['curr_position']}!")
                    p['curr_position'] = ladders[p['curr_position']]
                    print(f"{p['name']} 🔼 Climbed up to {p['curr_position']}")
                
                # Normal Movement Message.
                else:
                    print(f" {p['name']} ✅ Moved forward.")

            # More than 100 handling with Message.
            else:
                print(f"{p['name']} 🚫 Move not possible! You need exact number.")

        print(f"{p['name']} Current Position : {p['curr_position']}") # Printing Current Position.

        # --- WINNING CHECK ---
        if p['curr_position'] == 100:
            print("\n" + "="*40)
            print(f"🏆 WINNER IS {p['name']}! 🏆")
            print("="*40)
            Game_Over = True
            break # For loop tod do

    if Game_Over:
        break # While loop tod do
