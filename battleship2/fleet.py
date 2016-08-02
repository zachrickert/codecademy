"""The fleet class is a collection of ships for battleship game."""

import ship


class Fleet ():
    """A collection of ships."""

    def __init__(self):
        """Initialize the fleet."""
        self.sunk = False
        self.quit_flag = False
        self.ships = []
        battleship = ship.Battleship()
        submarine = ship.Submarine()
        self.ships.append(battleship)
        self.ships.append(submarine)

    def __str__(self):
        """Print Fleet status."""
        self.print_fleet()
        return ""

    def print_fleet(self):
        """Print the ships in the fleet."""
        for piece in self.ships:
            print(piece)

    def set_fleet(self, board):
        """Set up fleet."""
        for piece in self.ships:
            piece.set_location(board)
            if piece.quit_flag:
                self.quit_flag = True
                break

    def set_fleet_auto(self, board):
        """Set up fleet automatically."""
        for piece in self.ships:
            piece.set_location_auto(board)

    def set_damage(self, guess, guess_board):
        """Set damage for each member of the fleet."""
        for piece in self.ships:
            piece.set_damage(guess, guess_board)

    def all_ships_sank(self):
        """Check to see if any ships are still afloat."""
        for piece in self.ships:
            if not piece.sank:
                return False

        return True
