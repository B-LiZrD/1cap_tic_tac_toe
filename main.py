import random
from art import logo

board = [["1", "2", "3",], ["4", "X", "6"], ["7", "8", "9"]]


def DisplayBoard(board):
    """Board is made of print statements of strings and the 'board' list of lists"""
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def EnterMove(board):
    """Prompts valid input from player and returns a move_count of +1 """
    while True:
        move = int(input(" Where would you like to place your tac?\n '1-9': "))
        #   Checks to make sure input is valid
        if move < 1 or move > 9:
            print("Please pick a valid number")
            continue
        #   move converted into strings so that it can be compared with the contents of board
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print("That spot is taken already, please pick a different square... ")
            continue
        elif move == 1:
            board[0][0] = "O"
        elif move == 2:
            board[0][1] = "O"
        elif move == 3:
            board[0][2] = "O"
        elif move == 4:
            board[1][0] = "O"
        elif move == 6:
            board[1][2] = "O"
        elif move == 7:
            board[2][0] = "O"
        elif move == 8:
            board[2][1] = "O"
        elif move == 9:
            board[2][2] = "O"
        return


def MakeListOfFreeFields(board):
    """Appends all available fields to 'freeSquares' list. All 9 fields are checked"""
    freeSquares = []
    for row in range(0, 3):
        for column in range(0, 3):
            #   If square has "O" or "X", pass and resume iteration, otherwise, append the field to freeSquares
            if board[row][column] == "O" or board[row][column] == "X":
                pass
            else:
                freeSquares.append(([row], [column]))

    ## print(freeSquares)


def VictoryFor(board, sign):
    """Takes sign 'O' or sign 'X' and returns True if any of the conditions are True statements"""
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        ## print(f"Player {sign} is the winner")
        return True


def DrawMove(board):
    """A list of 1-9 but excluding '5' has a number randomly chosen using random.choice(). Similar to EnterMove(board),
    a field is populated that corresponds with the randomly selected number"""
    comp_lst = [1, 2, 3, 4, 6, 7, 8, 9]

    while True:
        computer_move = random.choice(comp_lst)
        ## print(computer_move)
        #   Checks if the board has a free space.  If this condition evaluates to true, the number that was randomly
        #   chosen gets eaten by continue, and a different number is picked
        if str(computer_move) not in board[0] and str(computer_move) not in board[1] and str(computer_move) not in board[2]:
            continue
        elif computer_move == 1:
            board[0][0] = "X"
            break
        elif computer_move == 2:
            board[0][1] = "X"
            break
        elif computer_move == 3:
            board[0][2] = "X"
            break
        elif computer_move == 4:
            board[1][0] = "X"
            break
        elif computer_move == 6:
            board[1][2] = "X"
            break
        elif computer_move == 7:
            board[2][0] = "X"
            break
        elif computer_move == 8:
            board[2][1] = "X"
            break
        elif computer_move == 9:
            board[2][2] = "X"
            break

#   Opening message
print(logo)
print("Welcome to Tic-Tac-Toe!")
DisplayBoard(board)
print()

#   Initialized to 1 because computer always goes first
move_count = 1
while move_count < 9:
    EnterMove(board)
    move_count += 1
    # DisplayBoard(board)

    if VictoryFor(board, "O") == True:
        print()
        print("Good job, you win!")
        break
    else:
        ## print("Here is the current list of free squares on the board: ")
        ## MakeListOfFreeFields(board)
        print()
        ## DisplayBoard(board)

    print()
    DrawMove(board)
    move_count += 1
    DisplayBoard(board)
    print()


    if VictoryFor(board, "X") == True:
        print()
        print("The computer has won! Better luck next time...")
        break
    else:
        ## print("Here is the current list of free squares on the board: ")
        ## MakeListOfFreeFields(board)
        print()
        # DisplayBoard(board)

else:
    #   Once the move_count is '9', a tie is declared
    print()
    print("We have a tie!")

print("Final board is: ")
DisplayBoard(board)

print("Play again soon, ok?")

