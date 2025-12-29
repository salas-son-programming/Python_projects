# Import the random module to allow the computer (O player)
# to choose a random available position
import random


# Create the game board as a list of 9 empty spaces
# Each index represents a position on the Tic-Tac-Toe board
board = [" " for i in range(9)]


# Function to display the board in a 3x3 grid format
def print_board():
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")


# Variable used to control the game loop
# When False, the game stops
check_winner = True


# Print the empty board at the start of the game
print_board()


# Function that returns all empty positions on the board
def get_available_positions():
    # enumerate gives (index, value)
    # we keep only positions where the value is a space
    return [i for i, val in enumerate(board) if val == " "]


# Function for the human player (X)
def x_player():
    # Ask the user to enter a position (1–9)
    square = int(input("Enter the index of the place : "))

    # Convert user input (1–9) to list index (0–8)
    square -= 1

    # If the chosen position is empty, place X
    if board[square] == " ":
        board[square] = "X"

    # If the position is already taken, ask again
    elif board[square] == "X" or board[square] == "0":
        print("You can't use this place")
        x_player()   # Recursive call until valid input


# Function for the computer player (O)
def o_player():
    # Get all available positions
    available_positions = get_available_positions()

    # Randomly choose one available position
    square = random.choice(available_positions)

    # Place O in the chosen position
    board[square] = "0"


# Function to check if there is a winner
def winner():
    global check_winner

    # Check all possible winning combinations

    # Rows
    if board[0] == board[1] == board[2] and board[0] != " ":
        print(f"{board[0]} won")
        check_winner = False
        print_board()

    if board[3] == board[4] == board[5] and board[3] != " ":
        print(f"{board[3]} won")
        check_winner = False
        print_board()

    if board[6] == board[7] == board[8] and board[6] != " ":
        print(f"{board[6]} won")
        check_winner = False
        print_board()

    # Columns
    if board[0] == board[3] == board[6] and board[0] != " ":
        print(f"{board[0]} won")
        check_winner = False
        print_board()

    if board[1] == board[4] == board[7] and board[1] != " ":
        print(f"{board[1]} won")
        check_winner = False
        print_board()

    if board[2] == board[5] == board[8] and board[2] != " ":
        print(f"{board[2]} won")
        check_winner = False
        print_board()

    # Diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        print(f"{board[0]} won")
        check_winner = False
        print_board()

    if board[2] == board[4] == board[6] and board[2] != " ":
        print(f"{board[2]} won")
        check_winner = False
        print_board()


# Start the game
print("x_player starts")

# First move by the human player
x_player()


# Main game loop
while check_winner:
    print("o_player's turn")
    print_board()

    # Computer plays
    o_player()

    # Check if someone has won
    winner()
