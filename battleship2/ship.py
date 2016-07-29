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
        location = self.location_input(board)
        if self.check_for_ships(board, location):
            self.place_ship(board, location)

    def location_input(self, board):
        """Gather the starting location of the ship."""
        print (board)
        start = input("Please input the upper left corner of the ship: ")
        start = Guess(start)
        if start.row > board.rows - self.length:
            if start.column > board.columns - self.length:
                print("Sorry, your ship is off the map.")
                self.set_location(board)
            else:
                direction = 'v'
        else:
            if start.column > board.columns - self.length:
                direction = 'h'
            else:
                direction = ""
                while not (direction == 'v' or direction == 'h'):
                    direction = input("(v)ertical or (h)orizontal?")
                    direction = direction.lower()
        return (start, direction)

    def check_for_ships(self, board, location):
        """Check for other ships already placed."""
        print (board.status[location[0].row][location[0].column])
        if location[1] == 'v':
            for i in range(self.length):
                if(board.status[location[0].row][location[0].column + i] != 'O'):
                    return False

        elif location[1] == 'h':
            for i in range(self.length):
                if(board.status[location[0].row + i][location[0].column] != 'O'):
                    return False

        else:
            print('GAME ERROR')
            return False

        return True

    def place_ship(self, board, location):
        """Place ship."""
        if location[1] == 'v':
            for i in range(self.length):
                board.status[location[0].row][location[0].column + i] = self.letter

        if location[1] == 'h':
            for i in range(self.length):
                board.status[location[0].row + i][location[0].column] = self.letter


class Battleship(Ship):
    """Battleship piece."""

    def __init__(self):
        """Initialize battleship."""
        Ship.__init__(self, "battleship", 4)
