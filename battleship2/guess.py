"""Class module to handle guesses.  Translates C4 -> (2, 3)."""
import functions
import sys


class Guess():
    """Turn a guess into a row and column."""

    def __init__(self, input_value):
        """Turn a guess into a row and column."""
        if input_value.lower == 'quit':
            sys.exit()
        self.input_value = input_value.upper()
        self.row = input_value[0]
        self.row = functions.let_to_numb(self.row) - 1
        self.column = int(input_value[1:]) - 1
        self.damage = functions.MISS

    def __str__(self):
        """Print the cell refernece for the guess."""
        return self.input_value

    def __eq__(self, other):
        """Return true if two guesses positions are the same."""
        if self.input_value == other.input_value:
            return True
        else:
            return False

    def position(self):
        """Return the cell reference for the guess."""
        return self.input_value
