import random

N = 8  # Number of queens

def conflicts(board):
    """Count number of attacking pairs"""
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j] or abs(board[i]-board[j]) == j-i:
                count += 1
    return count

def hill_climbing_nqueens():
    board = [random.randint(0, N-1) for _ in range(N)]
    while True:
        current_conflicts = conflicts(board)
        if current_conflicts == 0:
            return board
        best_board = list(board)
        best_conflicts = current_conflicts
        for col in range(N):
            for row in range(N):
                if row != board[col]:
                    temp = list(board)
                    temp[col] = row
                    temp_conflicts = conflicts(temp)
                    if temp_conflicts < best_conflicts:
                        best_conflicts = temp_conflicts
                        best_board = temp
        if best_conflicts == current_conflicts:
            board = [random.randint(0, N-1) for _ in range(N)]
        else:
            board = best_board

# Solve N-Queens
solution = hill_climbing_nqueens()
print("Queen positions (row for each column):", solution)
