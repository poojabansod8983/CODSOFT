import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column winner
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal winner
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal winner
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, maximizing_player):
    winner = check_winner(board)

    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row, col = map(int, input("Enter your move (row and column separated by space): ").split())
        if board[row][col] != ' ':
            print("Invalid move. Cell already occupied. Try again.")
            continue
        board[row][col] = 'X'

        # Check if player wins
        if check_winner(board) == 'X':
            print_board(board)
            print("Congratulations! You win!")
            break

        # Check if it's a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI's move
        ai_row, ai_col = best_move(board)
        print(f"AI plays at row {ai_row}, column {ai_col}")
        board[ai_row][ai_col] = 'O'

        # Check if AI wins
        if check_winner(board) == 'O':
            print_board(board)
            print("AI wins! Better luck next time.")
            break

if __name__ == "__main__":
    play_game()
