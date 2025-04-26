# Tic Tac Toe Game Using Tkinter

This is a simple Tic Tac Toe game built using Python's Tkinter library. It allows two players to play against each other on a 3x3 grid. The game detects a winner or a tie and allows restarting after each round.

## Features
- Interactive 3x3 grid GUI using Tkinter
- Alternating turns between Player X and Player O
- Automatic win or tie detection
- Pop-up messages to display game result
- One-click reset to start a new game

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

## How It Works
1.The game initializes a 3x3 button grid using Tkinter.
2.Each button represents a cell and updates to show the current player's mark ("X" or "O") on click.
3.A global list `board` tracks the state of the game.
4.After every move, the `check_winner()` function checks rows, columns, and diagonals for a win or tie.
5.If a winner or tie is detected, a messagebox popup shows the result, and the game is reset automatically.
6.The `reset_game()` function clears the board and restores turn to Player X.

