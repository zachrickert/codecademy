"""Ship class for the battleship game."""

from guess import Guess


class Ship():
    """Different ship pieces for the battleship game."""

    def __init__(self, name="error", length=1):
        """Initialize a single piece."""
        self.name = name.title()
        self.length = length
        self.letter = name[0].upper()
        self.sank = False
        self.damage = ['O'] * length

    def __str__(self):
        """Print ship type and damage."""
        str = "{} - [{}]".format(self.name, " ".join(self.damage))
        return str

    def set_location(self, board):
        """Set location for a ship on the board."""
        start = input("Please input the upper left corner of the ship: ")
        start = Guess(start)
        if start.row > board.rows - self.length:
            if start.column > board.column - self.length:
                print("Sorry you cannot put your ship there.  Part is off the map.")
            else:
                pass
                # set(start, "v")
        else:
            if start.column > board.column - self.length:
                pass
                # set(start, "h")
            else:
                direction = input("Do you want the ship to go (v)ertical or (h)orizontal?")


class Battleship(Ship):
    """Battleship piece."""

    def __init__(self):
        """Initialize battleship."""
        Ship.__init__(self, "battleship", 4)
