"""Battleship game."""

from random import randint


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


def random_row(board):
    """Return a random row."""
    return randint(0, len(board) - 1)


def random_col(board):
    """Return a random column."""
    return randint(0, len(board) - 1)


main()
