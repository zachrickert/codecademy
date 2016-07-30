"""The fleet class is a collection of ships for battleship game."""

import ship


class Fleet ():
    """A collection of ships."""

    def __init__(self):
        """Initialize the fleet."""
        self.sunk = False
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
