Browser_history = []
while True:

    user_input = input("Enter URL, type Back to go back or Exit:")
    
    if user_input.lower() == "back":

        if len(Browser_history) > 0:
            Browser_history.pop()
            if len(Browser_history) > 0:
                print(f"📍 Current Page: {Browser_history[-1]}")
            else:
                print("🏠 You are on the Home Page (History Empty).")
        else:
            print("No history to go back!")

    elif user_input.lower() == "exit":
        break
    else:
        if len(user_input) > 0:
            Browser_history.append(user_input)
            print(f"Current Page: {user_input}")
        else:
            print("Please Enter Valid URL")
