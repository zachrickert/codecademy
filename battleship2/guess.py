"""Class module to handle guesses.  Translates C4 -> (2, 3)."""
import functions


class Guess():
    """Turn a guess into a row and column."""

    def __init__(self, input_value):
        """Turn a guess into a row and column."""
        if input_value.lower() in ['quit', 'exit', 'q', 'e']:
            self.quit_flag = True
            self.row = -1
            self.column = -1
        else:
            self.quit_flag = False
            try:
                self.input_value = input_value.upper()
                self.row = input_value[0]
                self.row = functions.let_to_numb(self.row) - 1
                self.column = int(input_value[1:]) - 1
            except ValueError:
                print("Sorry, I do not understand")
                new_value = input("Enter another square: ")
                self.__init__(new_value)

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

    def check_if_on_board(self, board):
        """Check to see if input is on the game board."""
        while self.row >= board.rows or self.column >= board.columns:
            new_location = input("That is not on the board. Enter new square:")
            self.__init__(new_location)
