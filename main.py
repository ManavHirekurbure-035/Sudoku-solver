import numpy as np



def is_valid(board, row, col, num):
    # Check if num is not in the current row
    if num in board[row]:
        return False
    # Check if num is not in the current column
    if num in board[:, col]:
        return False
    # Check if num is not in the current 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if num in board[start_row:start_row + 3, start_col:start_col + 3]:
        return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Solved
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            if solve_sudoku(board):
                return True
            board[row, col] = 0
    return False

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                return (row, col)
    return None

# Example Sudoku Board
board = np.array([
    [0, 0, 0, 0, 8, 0, 0, 7, 0],
    [0, 5, 8, 0, 3, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 6, 0, 0, 0, 0, 9, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 6],
    [7, 0, 0, 0, 2, 9, 3, 0, 0],
    [0, 0, 7, 9, 0, 0, 9, 0, 0],
    [1, 0, 0, 0, 0, 3, 0, 0, 0],
    [5, 6, 0, 0, 0, 0, 0, 5, 4]
])

if solve_sudoku(board):
    print("Sudoku solved:")
    print(board)
else:
    print("No solution exists")
