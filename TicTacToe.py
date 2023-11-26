import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        # Initialize the board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Initialize current player
        self.current_player = 'X'

        # Create buttons for each cell
        self.buttons = [[tk.Button(root, text='', font=('normal', 20), width=6, height=2, command=lambda r=row, c=col: self.make_move(r, c)) for col in range(3)] for row in range(3)]

        # Place buttons on the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        # Check if the chosen cell is empty
        if self.board[row][col] == ' ':
            # Update the board
            self.board[row][col] = self.current_player

            # Update the button text
            self.buttons[row][col]['text'] = self.current_player

            # Check for a winner or a tie
            if self.check_winner():
                self.show_winner()
            elif self.is_board_full():
                self.show_tie()
            else:
                # Switch to the other player
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(cell == self.current_player for cell in self.board[i]) or all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        # Check if the board is full
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def show_winner(self):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_game()

    def show_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        # Reset the board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Clear button text
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''

        # Reset current player
        self.current_player = 'X'


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
