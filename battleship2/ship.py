"""Ship class for the battleship game."""
import functions

from guess import Guess


class Ship():
    """Different ship pieces for the battleship game."""

    def __init__(self, name="error", length=1):
        """Initialize a single piece."""
        self.name = name.title()
        self.length = length
        self.letter = name[0].upper()
        self.sank = False
        self.damage = [functions.EMPTY] * length
        self.quit_flag = False

    def __str__(self):
        """Print ship type and damage."""
        total_damage = ""
        for i in range(self.length):
            position_damage = self.damage[i].damage
            total_damage = total_damage + " " + (position_damage)
        str = "{} - [{}]".format(self.name, total_damage)
        return str

    def set_location(self, board):
        """Set location for a ship on the board."""
        location = self.location_input(board)
        self.quit_flag = location[0].quit_flag
        if not self.quit_flag:
            if self.check_for_ships(board, location):
                self.place_ship(board, location)
            else:
                board.message = 'That would cause your ships to overlap.'
                self.set_location(board)

    def set_location_auto(self, board):
        """Automatically sets the location of the ships."""
        location = self.location_input_auto(board)
        if self.check_for_ships(board, location):
            self.place_ship(board, location)
        else:
            self.set_location(board)

    def location_input_auto(self, board):
        """Randomize the location of the ships."""
        import random

        row = random.randint(1, board.rows)
        column = random.randint(1, board.columns)
        start = Guess(functions.numb_to_let(row) + str(column))

        if row > board.rows - self.length:
            if column > board.columns - self.length:
                start, direction = self.location_input_auto(board)
            else:
                direction = 'h'
        else:
            if column > board.columns - self.length:
                direction = 'v'
            else:
                if random.random() > 0.5:
                    direction = 'h'
                else:
                    direction = 'v'

        return (start, direction)

    def location_input(self, board):
        """Gather the starting location of the ship."""
        functions.clear()
        board.print_board()
        print("Place your {} - length {}.".format(self.name, self.length))
        start = input("Please input the upper left corner of the ship: ")
        start = Guess(start)
        if start.quit_flag:
            return (start, 'quit')

        if start.row >= board.rows or start.column >= board.columns:
            board.message = "Sorry, your ship is off the map."
            start, direction = self.location_input(board)
        elif start.row > board.rows - self.length:
            if start.column > board.columns - self.length:
                board.message = "Sorry, your ship is off the map."
                start, direction = self.location_input(board)
            else:
                direction = 'h'
        else:
            if start.column > board.columns - self.length:
                direction = 'v'
            else:
                direction = ""
                while not (direction == 'v' or direction == 'h'):
                    direction = input("(v)ertical or (h)orizontal?")
                    direction = direction.lower()
        return (start, direction)

    def check_for_ships(self, board, location):
        """Check for other ships already placed."""
        for i in range(self.length):
            if location[1] == 'v':
                row = location[0].row + i
                column = location[0].column
            elif location[1] == 'h':
                row = location[0].row
                column = location[0].column + i
            else:
                print('GAME ERROR')
                return False

            if(board.status[row][column] != functions.EMPTY):
                    return False

        return True

    def place_ship(self, board, location):
        """Place ship."""
        for i in range(self.length):
            if location[1] == 'v':
                row = location[0].row + i
                column = location[0].column
            else:
                row = location[0].row
                column = location[0].column + i

            board.status[row][column] = self.letter
            current_position = functions.rc_to_str(row, column)
            self.damage[i] = Guess(current_position)

        if board.name == "Computer":
            answer = "y"
        else:
            functions.clear()
            board.print_board()
            answer = ""

        while not (answer == 'y' or answer == 'n'):
            answer = input("Place ship here (y/n)? ")

        if answer == 'n':
            for i in range(self.length):
                if location[1] == 'v':
                    row = location[0].row + i
                    column = location[0].column
                else:
                    row = location[0].row
                    column = location[0].column + i

                board.status[row][column] = functions.EMPTY
            self.set_location(board)

    def set_damage(self, guess, guess_board):
        """Set damage on ships."""
        if guess in self.damage:
            self.damage[self.damage.index(guess)].damage = functions.HIT
            if self.ship_sunk():
                self.sank = True
                guess_board.message += " {} sank!".format(self.name)

    def ship_sunk(self):
        """Test to see if a ship is sunk."""
        for i in range(self.length):
            if self.damage[i].damage == functions.MISS:
                return False

        return True


class Battleship(Ship):
    """Battleship piece."""

    def __init__(self):
        """Initialize battleship."""
        Ship.__init__(self, "battleship", 4)


class Submarine(Ship):
    """Submarine piece."""

    def __init__(self):
        """Initialize battleship."""
        Ship.__init__(self, "submarine", 3)
