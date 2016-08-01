"""Game class for the battleship game."""

import functions

from board import Board
from fleet import Fleet
from guess import Guess

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
        self.done = False

        self.user_board = Board(self.name)
        self.computer_board = Board("Computer")
        self.guess_board = Board("Guesses")
        self.user_fleet = Fleet()
        self.user_fleet.set_fleet(self.user_board)
        self.computer_fleet = Fleet()
        self.computer_fleet.set_fleet_auto(self.computer_board)
        self.play_game()

    def print_game_status(self):
        """Print the current game status."""
        self.guess_board.print_board()
        # self.computer_board.print_board()
        print('=' * self.user_board.columns * 4)
        self.user_board.print_board()

    def play_game(self):
        """Battleship Game mechanics."""
        turn_count = 0
        print(self.computer_fleet)
        while not self.done:
            functions.clear()
            self.print_game_status()
            user_guess = input("Please Enter a Guess: ")
            user_guess = Guess(user_guess)
            self.computer_board.check_damage(user_guess,
                                             self.guess_board,
                                             self.computer_fleet)
            turn_count += 1
            if turn_count >= 100:
                self.done = True

myGame = Game()
