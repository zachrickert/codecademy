"""Common functions for the battleship game."""


EMPTY = '-'
MISS = 'o'
HIT = '*'


def let_to_numb(str):
    """Change letter to number."""
    return ord(str.upper()) - 64


def numb_to_let(numb):
    """Change a number into a letter."""
    return chr(numb + 64)


def rc_to_str(row, column):
    """Change a row and column input to a string input."""
    row = numb_to_let(row + 1)
    column = str(column + 1)
    return row + column


def clear():
    """Clear the screen."""
    import os

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
