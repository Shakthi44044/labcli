# Tic-Tac-Toe board (0 = empty, 'X', 'O')
board = [' ' for _ in range(9)]

# Check for win
def check_win(b, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b1,c in wins:
        if b[a]==b[b1]==b[c]==player:
            return True
    return False

# Minimax function
def minimax(b, is_max):
    if check_win(b, 'X'): return 1
    if check_win(b, 'O'): return -1
    if ' ' not in b: return 0
    if is_max:
        best = -float('inf')
        for i in range(9):
            if b[i]==' ':
                b[i]='X'
                best = max(best, minimax(b, False))
                b[i]=' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if b[i]==' ':
                b[i]='O'
                best = min(best, minimax(b, True))
                b[i]=' '
        return best

# Find best move for X
def best_move():
    best_val = -float('inf')
    move = -1
    for i in range(9):
        if board[i]==' ':
            board[i]='X'
            val = minimax(board, False)
            board[i]=' '
            if val > best_val:
                best_val = val
                move = i
    return move

# Example usage
board = ['X','O','X',
         ' ','O',' ',
         ' ',' ',' ']
move = best_move()
print("Best move for X is at position:", move)
