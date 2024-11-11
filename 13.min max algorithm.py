import math

# Constants for player representation
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '


def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")
    print()


def evaluate(board):
    """Evaluate the current state of the board."""
    # Check rows
    for row in board:
        if all(cell == PLAYER_X for cell in row):
            return 10
        elif all(cell == PLAYER_O for cell in row):
            return -10

    # Check columns
    for col in range(3):
        if all(board[row][col] == PLAYER_X for row in range(3)):
            return 10
        elif all(board[row][col] == PLAYER_O for row in range(3)):
            return -10

    # Check diagonals
    if all(board[i][i] == PLAYER_X for i in range(3)) or all(board[i][2 - i] == PLAYER_X for i in range(3)):
        return 10
    elif all(board[i][i] == PLAYER_O for i in range(3)) or all(board[i][2 - i] == PLAYER_O for i in range(3)):
        return -10

    # If no winner yet
    return 0


def is_moves_left(board):
    """Check if there are any empty cells left."""
    for row in board:
        if EMPTY in row:
            return True
    return False


def minimax(board, depth, is_maximizing):
    """Minimax algorithm implementation."""
    score = evaluate(board)

    # Base cases - terminal states (win/lose/draw)
    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif not is_moves_left(board):
        return 0

    # If maximizing player's turn (X)
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = EMPTY
        return best

    # If minimizing player's turn (O)
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minimax(board, depth + 1, not is_maximizing))
                    board[i][j] = EMPTY
        return best


def find_best_move(board):
    """Find the best move using Minimax."""
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move


def main():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]

    print("Initial Board:")
    print_board(board)

    while is_moves_left(board):
        # Player X's turn (Human)
        print("Player X's turn (Human)")
        while True:
            x = int(input("Enter row number (0-2): "))
            y = int(input("Enter column number (0-2): "))
            if board[x][y] == EMPTY:
                board[x][y] = PLAYER_X
                break
            else:
                print("Invalid move. Cell is not empty. Try again.")

        print_board(board)

        # Check if X wins
        if evaluate(board) == 10:
            print("Player X wins!")
            break

        # Check for a draw
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # Player O's turn (Computer)
        print("Player O's turn (Computer)")
        x_o, y_o = find_best_move(board)
        board[x_o][y_o] = PLAYER_O

        print_board(board)

        # Check if O wins
        if evaluate(board) == -10:
            print("Player O wins!")
            break

        # Check for a draw
        if not is_moves_left(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()