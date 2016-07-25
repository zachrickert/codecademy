"""Battleship game."""

from random import randint


ROWS = 5
COLUMNS = 12
TURNS = 4


def main():
    """Battleship game."""
    board = []
    set_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(1, TURNS + 1):
        print('\n\n')
        print('Guess #{} out of {}'.format(turn, TURNS))
        print('=' * 20)
        print_board(board)
        guess_row = input("Guess Row (A - {}): ".format(numb_to_let(ROWS)))
        guess_row = let_to_numb(guess_row) - 1
        guess_col = int(input("Guess Col (1 - {}): ".format(COLUMNS))) - 1

        if (guess_row == ship_row and guess_col == ship_col):
            print ("Congratulations! You sank my battleship!")
            break
        else:
            if (guess_row >= ROWS or guess_col >= COLUMNS):
                print("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == 'X'):
                print("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = 'X'
                if turn >= 4:
                    print("Game Over.")


def set_board(board):
    """Set up starting board."""
    for x in range(ROWS):
        board.append(["O"] * COLUMNS)


def print_board(board):
    """Print the game grid."""
    for row in range(-2, ROWS):
        for column in range(COLUMNS):
            if column + 1 < 10:
                whitespace = 2
            else:
                whitespace = 1
            if row == -2:
                if column == 0:
                    print("    ", end="")
                print ("{}{}".format(column + 1, " " * whitespace), end="")
            elif row == -1:
                if column == 0:
                    print("   ", end="")
                print("{}".format("-" * 3), end="")
            else:
                if column == 0:
                    print("{} | ".format(numb_to_let(row + 1)), end="")

                print("{}{}".format(board[row][column], "  "), end="")
        if column == COLUMNS - 1:
            print()


def print_board_old(board):
    """Print the game grid."""
    print("    ", end="")
    for column_number in range(COLUMNS):
        print ("{} ".format(column_number + 1), end="")
    print()
    print("    ", end="")
    print('-' * (1 + column_number * 2))
    for row_number, row in enumerate(board):
        print("{} | ".format(numb_to_let(row_number + 1)), end="")
        print (" ".join(row))


def random_row(board):
    """Return a random row."""
    return randint(0, ROWS - 1)


def random_col(board):
    """Return a random column."""
    return randint(0, COLUMNS - 1)


def numb_to_let(numb):
    """Change a number into a letter."""
    return chr(numb + 64)


def let_to_numb(str):
    """Change letter to number."""
    return ord(str.upper()) - 64

main()
