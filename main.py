import tkinter as tk
from tkinter import messagebox

# Initialize the game window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
player_turn = "X"
board = [""] * 9  # A list to keep track of the board state

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]  # Return the winning player ("X" or "O")
    if "" not in board:
        return "Tie"  # Return "Tie" if the board is full and no winner
    return None  # No winner yet

# Button click handler
def button_click(index):
    global player_turn
    if board[index] == "":  # Only allow clicking empty buttons
        board[index] = player_turn
        buttons[index].config(text=player_turn)
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            reset_game()
        else:
            # Switch turns
            player_turn = "O" if player_turn == "X" else "X"

# Function to reset the game
def reset_game():
    global player_turn, board
    player_turn = "X"
    board = [""] * 9
    for button in buttons:
        button.config(text="")

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Helvetica", 20), height=2, width=5, 
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)  # Arrange buttons in a 3x3 grid
    buttons.append(button)

# Run the game loop
root.mainloop()
