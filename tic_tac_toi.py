import copy

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the current player has won
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3))
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is over
def game_over(board):
    return any(check_winner(board, player) for player in ["X", "O"]) or all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to evaluate the game state
def evaluate(board):
    if check_winner(board, "X"):
        return 1
    if check_winner(board, "O"):
        return -1
    return 0

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, maximizing, alpha, beta):
    if depth == 0 or game_over(board):
        return evaluate(board)
    
    if maximizing:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth - 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth - 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move using minimax
def find_best_move(board):
    best_eval = float("-inf")
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 5, False, float("-inf"), float("inf"))
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    
    return best_move

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while not game_over(board):
        display_board(board)
        
        if current_player == "X":
            row, col = find_best_move(board)
        else:
            while True:
                try:
                    row = int(input("Enter the row (0, 1, 2): "))
                    col = int(input("Enter the column (0, 1, 2): "))
                except ValueError:
                    print("Invalid input. Please enter numbers between 0 and 2.")
                    continue
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
        
        board[row][col] = current_player
        current_player = "X" if current_player == "O" else "O"

    display_board(board)

    if check_winner(board, "X"):
        print("AI (X) wins!")
    elif check_winner(board, "O"):
        print("Human (O) wins!")
    else:
        print("It's a draw!")

# Start the game
if __name__ == "__main__":
    play_game()
