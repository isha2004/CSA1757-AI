def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Checks if the specified player has won."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def main():
    board = [[' '] * 3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")

        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
                if board[row][col] == ' ':
                    break
                else:
                    print("That cell is already occupied. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
            except IndexError:
                print("Invalid input. Please enter row and column numbers within 0 to 2.")

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Congratulations! Player {players[current_player]} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = (current_player + 1) % 2


if __name__ == "__main__":
    main()