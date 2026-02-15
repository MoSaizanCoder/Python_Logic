board = [" "," "," "," "," "," "," "," "," "]

turn = "X"

while True:
    print(board[0:3])
    print(board[3:6])
    print(board[6:])

    # ------- Taking Input ------
    user_input_index = int(input(f"Enter a index from 1-9 for ({turn}) : "))

    # --------- Input Check -------
    if 0 < user_input_index < 10:

        # ------------- Update Logic If Empty ------------- 
        if board[user_input_index - 1] == " ":
            board[user_input_index - 1] = turn  

            # ---------- Winning Logic -------------
            if (board[0] == board[1] == board[2] != " ") or \
        (board[3] == board[4] == board[5] != " ") or \
        (board[6] == board[7] == board[8] != " ") or \
        (board[0] == board[3] == board[6] != " ") or \
        (board[1] == board[4] == board[7] != " ") or \
        (board[2] == board[5] == board[8] != " ") or \
        (board[0] == board[4] == board[8] != " ") or \
        (board[2] == board[4] == board[6] != " "):
                print(board[0:3])
                print(board[3:6])
                print(board[6:])
                print(f"Winner is.. : {turn}")
                break

            # ------------Match Draw Logic -------------
            if " " not in board:
                print(board[0:3])
                print(board[3:6])
                print(board[6:])
                print("Game Over Match Draw")
                break

            # ------ Player Turn Switching Logic ----------------
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        
        else:
            print("Invalid Index Its Already full")

    else:
        print("Invalid Input Please Enter Integer between 1 - 9.")