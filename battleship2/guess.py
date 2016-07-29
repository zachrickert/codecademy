"""Class module to handle guesses.  Translates C4 -> (3, 4)."""


class Guess():
    """Turn a guess into a row and column."""

    def __init__(self, input_value):
        """Turn a guess into a row and column."""
        self.row = input_value[0]
        self.row = let_to_numb(self.row) - 1
        self.column = int(input_value[1:]) - 1


def let_to_numb(str):
    """Change letter to number."""
    return ord(str.upper()) - 64
