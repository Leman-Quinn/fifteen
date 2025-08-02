from time import sleep
import random

Q = 20

def tittle():
    print(f"+++ F  I  F  T  E  E  N +++")

def exit():
    while True:
        key = input("Enter any key to exit")
        if key != "":
            exit()

def rules():
    print(f"\nRules: ")
    sleep(0.5)
    print(f"Sort all the numbers in the last amount of movements.")
    sleep(0.5)
    print(f"Movements are up, down, left and right.")
    sleep(0.5)
    print(f"You can also queue multiple inputs at once!")
    main()

def flair():
    sleep(0.85)
    print("\nGenerating board . . .",)
    sleep(1)
    print("\nScrambling numbers . . .")
    sleep(2)
    print("\nPerforming complex ecuations and calculations . .")
    sleep(0.374)
    print("\nSolutions found in 0.374 seconds. Record efficiency detected.")
    sleep(1)
    print("\nHave fun.")
    sleep(0.5)       
    print("(Mandatory)")
    print("\n")
    sleep(1)

def printBoard(board, rows, columns):
    for row in range(int(rows)): 
        for column in range(int(columns)):
            print(f"{board[row][column]:^3}", end=" ")
        print(" ")

def generateBoards(total_pieces, num_rows, num_columns):
    #Generates playable and winner board
    numberToAdd = 1
    playerBoard = []
    winerBoard = []

    for row in range(int(num_rows)):
                
                row = []

                for column in range(int(num_columns)):

                    if numberToAdd < total_pieces:

                        row.append(numberToAdd)

                        numberToAdd += 1

                    else:
                        row.append(0)

                playerBoard.append(row)
                winerBoard.append(row)

    return playerBoard, winerBoard

def randomizePlayerBoard(board, num_rows, num_columns):

    for i in range(Q):

        possibleMovements = ("w","a","s","d")

        if random.choice(possibleMovements) == "w":

            move_up(board, num_rows, num_columns)

        elif random.choice(possibleMovements) == "s":

            move_down(board, num_rows, num_columns)

        elif random.choice(possibleMovements) == "d":
             
             move_right(board, num_rows, num_columns)

        else:

            move_left(board, num_rows, num_columns)    

def move_up(board, rows, columns):

    zero_i = None
    zero_j = None

    for row in range(rows):

        for column in range(columns):

            if board[row][column] == 0:
                zero_i = row
                zero_j = column

                break
            else:
                continue

    if (zero_i - 1) >= 0:
        board[zero_i][zero_j], board[zero_i-1][zero_j] = board[zero_i-1][zero_j], board[zero_i][zero_j]

def move_down(board, rows, columns):
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

def main():
        """Main body that houses the structure and overall functions of the program itself."""
        user_input = input("\nStart -> 1\nRules -> 2\nExit -> 3\n")
        if user_input == "1":

            num_rows = input("How many rows should the board have?   ")
            num_columns = input("And what about columns?    ")
            total_pieces = int(num_rows) * int(num_columns)
            board, win_board = generateBoards(total_pieces, num_rows, num_columns)
            moves_counter = 0
            
            if num_rows == "1" or num_columns == "1": #avoids creating rows and/or columns of length 1
                print("\nThe number of rows and/or columns must be higher than 1.")
                return main()
            
            flair() #flavor
            randomizePlayerBoard(board, num_rows, num_columns)
            printBoard(board, num_rows, num_columns)

            while True:
                if board == win_board: #checks for winning conditions
                    print(f"Congrats! You've won in a total of {moves_counter} moves!")
                    sleep(1)
                    exit()
                elif moves_counter == (Q * 5):
                    print(f"You have exceded the maximum number of movements permited for this match.")
                    user_movement = input("\nRestart -> 1\nExit -> 2   ")

                    if user_movement == "1":
                        main()
                    elif user_movement == "2":
                        exit()
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
                            exit()
                        else:
                            sleep(0.5)
                            print("\nPlease enter a valid move.\n")
                            sleep(0.5)
                    printBoard(board, num_rows, num_columns)
        elif user_input == "2":
            rules()
        elif user_input == "3":
            exit()

tittle()
main()