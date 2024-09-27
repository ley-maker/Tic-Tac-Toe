# A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turns inputting their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# Function to update the game board with the user input
def markBoard(position, mark):
    if position in board:
        board[position] = mark

# Function to print the game board as described at the top
def printBoard():
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[7]} | {board[8]} | {board[9]}")

# Function to check for wrong input, this function should return True or False.
# It checks for invalid positions, or if the position is already occupied
def validateMove(position):
    try:
        position = int(position)  # Convert the input to an integer
        if 1 <= position <= 9 and board[position] == ' ':  # Check if valid move
            return True
        return False
    except ValueError:
        return False  # Return False if conversion to int fails

# List of winning combinations for the game
winCombinations = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
    [1, 5, 9], [3, 5, 7]              # diagonals
]

# Function to check if the player has won
def checkWin(player):
    for combo in winCombinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

# Function to check if the game board is already full (tie)
def checkFull():
    return all(space != ' ' for space in board.values())

# Main game loop
gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
      ' 1 | 2 | 3 \n' +
      ' --------- \n' +
      ' 4 | 5 | 6 \n' +
      ' --------- \n' +
      ' 7 | 8 | 9 \n')

# Main game loop logic
while not gameEnded:
    printBoard()
    
    move = input(currentTurnPlayer + "'s turn, input (1-9): ")
    
    # Validate the move
    if not validateMove(move):
        print("Invalid move, please try again.")
        continue
    
    # Mark the board
    markBoard(int(move), currentTurnPlayer)
    
    # Check if the current player wins
    if checkWin(currentTurnPlayer):
        printBoard()
        print(f"Player {currentTurnPlayer} wins!")
        gameEnded = True
        break
    
    # Check if the board is full (tie)
    if checkFull():
        printBoard()
        print("It's a tie!")
        gameEnded = True
        break
    
    # Switch player
    currentTurnPlayer = 'O' if currentTurnPlayer == 'X' else 'X'
1