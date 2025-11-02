import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"
]

currentPlayer = "X"
isRunning = True
winner = None

# display the board
def displayBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    



# taking user input
def takeUserInput(board):
    inp = int(input("Enter a number 1- 9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = "X"
        
    else:
        print("Oops! spot already taken")
        
        
def switchUser():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
        
def computer(board):
    global currentPlayer
    while currentPlayer != "X":
        position  = random.randint(0,8)
        if  board[position - 1] == "-":
            board[position - 1] = "O"
            switchUser()

def checkPositions(board):
    global winner
    #horizontal check
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[8]
        return True
    
    # Row check
    elif board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[7] != "-":
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[5]
        return True
    
    # check diagonal
    elif board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkwin():
    global isRunning
    if checkPositions(board):
        print(f"You win {winner}")
        isRunning = False
    

def checkTie(board):
    if "-" not in board:
        print("it is a tie")



while isRunning:
    displayBoard(board)
    takeUserInput(board)
    switchUser()
    computer(board)
    checkwin()
    checkTie(board)
    