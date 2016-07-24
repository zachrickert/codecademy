"""Battleship game."""


def main():
    """Battleship game."""
    board = []

    for i in range(5):
        board.append(["O"] * 5)

    print_board(board)


def print_board(board):
    """Print the game grid."""
    for row in board:
        print (" ".join(row))


main()
