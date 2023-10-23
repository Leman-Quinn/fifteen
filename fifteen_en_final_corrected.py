#Fifteen
from time import sleep
import random

Q = 20


def intro():
    """Displays the game tittle."""

    print(f"< < < F  I  F  T  E  E  N > > >")


def close():
    """Exits the program after inputing any key."""

    while True:

        exit_keyword = input("Enter any key to exit   ")
        if exit_keyword != "":
            exit()


def rules():
    """Shows the rules."""

    print(f"\nRules: ")
    sleep(1)
    print(f"To be able to sort all the given randomized numbers in the last amount of movements.")
    sleep(1)
    print(f"Movements are defined by up, down, left and right. Additionally, several movements can be input at once.")
    main()


def yassifier():
    """"Beauty is also important, queen. Periot."""

    sleep(0.85)
    print("\nGenerating board . . .",)
    sleep(2)
    print("\nScrambling numbers . . .")
    sleep(1)
    print("\nPerforming complex ecuations and calculations . .")
    sleep(0.374)
    print("\nSolutions found in 0.374 seconds. Record efficiency detected.")
    sleep(1)
    print("\nHave fun.")
    sleep(0.5)       
    print("(Mandatory)")
    print("\n")
    sleep(2)


def printer(board, rows, columns):
    """Formats and displays the board according to the parameters given."""

    for row in range(int(rows)): 

        for column in range(int(columns)):

            print(f"{board[row][column]:^3}", end=" ")

        print(" ")


def move_up(board, rows, columns):
    """Moves the zero upwards."""

    zero_i = None
    zero_j = None

    for i in range(int(rows)): #finds coordinate i and j for the zero

        for j in range(int(columns)):

            if board[i][j]==0:
                zero_i = i
                zero_j = j
            else:
                continue

    if (zero_i-1)>=0: #avoids going out of list range
        board[zero_i][zero_j], board[zero_i-1][zero_j] = board[zero_i-1][zero_j], board[zero_i][zero_j] #performs the switch


def move_down(board, rows, columns):
    """Moves the zero downwards."""

    zero_i = None
    zero_j = None

    for i in range(int(rows)): #finds the i and j coordinate for the zero

        for j in range(int(columns)):

            if board[i][j]==0:
                zero_i = i
                zero_j = j
            else:
                continue

    if (zero_i+1)<int(rows): #avoids going out of list range
        board[zero_i][zero_j], board[zero_i+1][zero_j] = board[zero_i+1][zero_j], board[zero_i][zero_j] #performs the switch


def move_left(board, rows, columns):
    """Moves the zero leftward."""

    zero_i = None
    zero_j = None

    for i in range(int(rows)): #finds the i and j coordinate for the zero

        for j in range(int(columns)):

            if board[i][j]==0:
                zero_i = i
                zero_j = j
            else:
                continue

    if (zero_j-1)>=0: #avoids going out of list range
        board[zero_i][zero_j], board[zero_i][zero_j-1] = board[zero_i][zero_j-1], board[zero_i][zero_j] #performs the switch


def move_right(board, rows, columns):
    """Moves the zero rightward."""

    zero_i = None
    zero_j = None

    for i in range(int(rows)): #finds the i and j coordinate for the zero

        for j in range(int(columns)):

            if board[i][j]==0:
                zero_i = i
                zero_j = j
            else:
                continue

    if (zero_j+1)<int(columns): #avoids going out of list range
        board[zero_i][zero_j], board[zero_i][zero_j+1] = board[zero_i][zero_j+1], board[zero_i][zero_j] #performs the switch


def board_generator(total_pieces, num_rows, num_columns):
    """Generates the playable board(dynamic) and winner board(static)."""
    
    current_number = 1 #how the numbers are assigned when generating the board
    board = []
    win_board = []

    for rows in range(int(num_rows)): #generates the board
                rows = []

                for columns in range(int(num_columns)):
                    if current_number < total_pieces:
                        rows.append(current_number)
                        current_number += 1
                    else:
                        rows.append(0)

                board.append(rows)
                win_board.append(list(rows))
        
    return board, win_board


def randomizer(board, num_rows, num_columns):
    for i in range(Q):

        possible_movements = ("w","a","s","d")

        if random.choice(possible_movements)=="w":
            move_up(board, num_rows, num_columns)
        elif random.choice(possible_movements)=="s":
            move_down(board, num_rows, num_columns)
        elif random.choice(possible_movements)=="d":
             move_right(board, num_rows, num_columns)
        else:
            move_left(board, num_rows, num_columns)    


def main():
        """Main body that houses the structure and overall functions of the program itself."""
        user_input = input("\nStart -> 1\nRules -> 2\nExit -> 3\n")
        if user_input == "1":
            
            num_rows = input("How many rows should the board have?   ")
            num_columns = input("And what about columns?    ")
            total_pieces = int(num_rows) * int(num_columns)
            board, win_board = board_generator(total_pieces, num_rows, num_columns)
            moves_counter = 0
            
            if num_rows == "1" or num_columns == "1": #avoids creating rows and/or columns of length 1
                print("\nThe number of rows and/or columns must be higher than 1.")
                return main()
            
            yassifier() #flavor
            randomizer(board, num_rows, num_columns)
            printer(board, num_rows, num_columns)

            while True:
                
                if board == win_board: #checks for winning conditions
                    print(f"Congrats! You've won in a total of {moves_counter} moves!")
                    sleep(1)
                    close()
                elif moves_counter == (Q * 5):
                    print(f"You have exceded the maximum number of movements permited for this match.")
                    user_movement = input("\nRestart -> 1\nExit -> 2   ")

                    if user_movement == "1":
                        main()
                    elif user_movement == "2":
                        close()
                else:
                    print(f"Controls: w, a, s, d")
                    print(f"Moves made: {moves_counter}")
                    print(f"Maximum moves allowed: {Q * 5}")
                    print(f"Exit -> 2")
                    user_movement = input("\nMake a move:   ")
                    moves = list(user_movement)

                    for move in moves:

                        if move.lower() == "w":
                            move_up(board, num_rows, num_columns)
                            moves_counter += 1 
                        elif move.lower() == "s":
                            move_down(board, num_rows, num_columns)
                            moves_counter += 1
                        elif move.lower() == "d":
                            move_right(board, num_rows, num_columns)
                            moves_counter += 1
                        elif move.lower() == "a":
                            move_left(board, num_rows, num_columns)
                            moves_counter += 1
                        elif move == "2":
                            close()
                        else:
                            sleep(0.5)
                            print("\nPlease enter a valid move.\n")
                            sleep(0.5)

                    printer(board, num_rows, num_columns)
        elif user_input == "2":
            rules()
        elif user_input == "3":
            close()


intro()

main()
