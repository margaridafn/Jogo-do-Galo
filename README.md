# Jogo-do-Galo

This repository contains a simple command-line implementation of the game Tic-Tac-Toe, known as *Jogo do Galo* in Portuguese. This project was developed as the final assignment for the Python Essentials 1 course.

## Gameplay

This is a single-player game where you compete against the computer.

*   The game is played on a 3x3 grid.
*   You play as 'O', and the computer plays as 'X'.
*   The computer always makes the first move by placing an 'X' in the center square.
*   Players take turns placing their marks in empty squares.
*   The first player to align three of their marks horizontally, vertically, or diagonally wins.
*   If all squares are filled and no one has won, the game results in a draw.

## How to Play

1.  Ensure you have Python 3 installed on your system.
2.  Clone or download this repository to your local machine.
3.  Open a terminal or command prompt and navigate to the project directory.
4.  Run the game with the following command:

    ```sh
    python Jogo.py
    ```
5.  The game board will be displayed. When it is your turn, enter a number from 1 to 9 corresponding to the square where you want to place your 'O'.

## Code Overview

The entire game logic is contained within the `Jogo.py` script. Here is a breakdown of the main functions:

*   `display_board(board)`: Renders the current state of the 3x3 game board in the console.
*   `enter_move(board)`: Handles the human player's turn. It prompts for input, validates that the chosen square is valid and unoccupied, and then updates the board with an 'O'.
*   `make_list_of_free_fields(board)`: Scans the board and returns a list of all currently empty squares.
*   `victory_for(board, sgn)`: Checks if the player with the given sign ('X' or 'O') has achieved a winning combination.
*   `draw_move(board)`: Executes the computer's turn by randomly selecting one of the available free squares and placing an 'X' on it.

The script initializes the board, sets the computer's first move in the center, and then enters a loop that alternates turns between the user and the computer until a win or draw condition is met.