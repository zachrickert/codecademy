"""Game class for the battleship game."""

from board import Board
from fleet import Fleet

"""Battleship versus an AI opponet.
1. Create a board
2. Set pieces.
3. Ask for guess.
4. Reply hit or miss.
5. Computer guess
6. Check win condition."""


class Game():
    """Game clas for Battleship."""

    def __init__(self):
        """Initialize the game."""
        self.level = 'normal'
        self.name = input("Please enter your name: ")

        self.user_board = Board(self.name)
        self.computer_board = Board("Computer")
        self.user_fleet = Fleet()
        self.user_fleet.set_fleet(self.user_board)

    def __str__(self):
        """Print the current game status."""
        self.print_game_status()
        return ""

    def print_game_status(self):
        """Print the current game status."""
        print(myGame.user_board)
        print('=' * myGame.user_board.columns * 3)
        print(myGame.computer_board)


myGame = Game()
