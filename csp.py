def solve_n_queens(n):
    board = [-1] * n
    return backtrack(board, 0)
def backtrack(board, row):
    if row == len(board):
        return board
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            result = backtrack(board, row + 1)
            if result is not None:
                return result
            board[row] = -1
    return None
def is_valid(board, row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True
def print_board(board):
    for row in board:
        line = ''
        for col in row:
            if col == -1:
                
                line += 'Q '
            else:
                line += '. '
        print(line)
    print()
n = 4
solution = solve_n_queens(n)
if solution is not None:
    board = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        board[i][solution[i]] = 1
    print_board(board)
else:
    print(f"No solution found for {n}-Queens problem.")
