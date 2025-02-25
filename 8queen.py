#8queen safe 

def is_safe(board, row, col):
    # Check column and diagonals
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row):
    if row == 8:  # All queens placed
        solutions.append(board[:])
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            solve_n_queens(board, row + 1)  # Recur for next row

def print_solution():
    for sol in solutions:
        for r in range(8):
            print(" ".join("Q" if sol[r] == c else "." for c in range(8)))
        print("\n" + "-"*16)

# Initialize and solve
solutions = []
solve_n_queens([-1] * 8, 0)
print_solution()
