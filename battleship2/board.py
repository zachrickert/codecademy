"""Board class for the battleship game."""
import functions


class Board():
    """Board class for battleship game."""

    def __init__(self, name="No Name"):
        """Initialize a new game board."""
        self.rows = 10
        self.columns = 10
        self.name = name

        self.status = []
        for row in range(self.rows):
            self.status.append(["O"] * self.columns)

    def __str__(self):
        """Print the currnet status of the game."""
        self.print_board()
        return ""

    def print_board(self):
        """Print the current status of the game."""
        for row in range(-2, self.rows):
            for column in range(self.columns):
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
                        letter = functions.numb_to_let(row + 1)
                        print("{} | ".format(letter), end="")

                    print("{}{}".format(self.status[row][column], "  "),
                          end="")
            if column == self.columns - 1:
                print()