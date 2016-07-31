"""Class module to handle guesses.  Translates C4 -> (2, 3)."""
import functions


class Guess():
    """Turn a guess into a row and column."""

    def __init__(self, input_value):
        """Turn a guess into a row and column."""
        self.input_value = input_value
        self.row = input_value[0]
        self.row = functions.let_to_numb(self.row) - 1
        self.column = int(input_value[1:]) - 1

    def __str__(self):
        """Print the cell refernece for the guess."""
        return self.input_value
