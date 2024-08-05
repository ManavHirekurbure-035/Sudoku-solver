import tkinter as tk
from tkinter import messagebox
import numpy as np

class SudokuUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.geometry("400x450")
        self.grid_size = 9
        self.entries = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                entry = tk.Entry(self, width=3, font=('Arial', 16), borderwidth=2, relief="solid", justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry
        
        solve_button = tk.Button(self, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=self.grid_size, column=0, columnspan=self.grid_size, pady=10)

    def get_board(self):
        board = np.zeros((self.grid_size, self.grid_size), dtype=int)
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                value = self.entries[row][col].get()
                if value.isdigit():
                    board[row][col] = int(value)
        return board

    def set_board(self, board):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.entries[row][col].delete(0, tk.END)
                if board[row][col] != 0:
                    self.entries[row][col].insert(0, str(board[row][col]))

    def is_valid(self, board, row, col, num):
        if num in board[row]:
            return False
        if num in board[:, col]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        if num in board[start_row:start_row + 3, start_col:start_col + 3]:
            return False
        return True

    def solve_sudoku(self):
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)
        else:
            messagebox.showinfo("Result", "No solution exists")

    def solve(self, board):
        empty = self.find_empty_location(board)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row, col] = num
                if self.solve(board):
                    return True
                board[row, col] = 0
        return False

    def find_empty_location(self, board):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if board[row, col] == 0:
                    return (row, col)
        return None

if __name__ == "__main__":
    app = SudokuUI()
    app.mainloop()
