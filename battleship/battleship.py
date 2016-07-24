"""Battleship game."""

from random import randint


ROWS = 5
COLUMNS = 10
TURNS = 4


def main():
    """Battleship game."""
    board = []
    set_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print(ship_row, ship_col)

    for turn in range(1, TURNS + 1):
        print('\n\n')
        print('Guess #{} out of {}'.format(turn, TURNS))
        print('=' * 20)
        print_board(board)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if (guess_row == ship_row and guess_col == ship_col):
            print ("Congratulations! You sank my battleship!")
            break
        else:
            if (guess_row >= ROWS or guess_col >= COLUMNS):
                print("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == 'X'):
                print("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = 'X'
                if turn >= 4:
                    print("Game Over.")


def set_board(board):
    """Set up starting board."""
    for x in range(ROWS):
        board.append(["O"] * COLUMNS)


def print_board(board):
    """Print the game grid."""
    for row in board:
        print (" ".join(row))


def random_row(board):
    """Return a random row."""
    return randint(0, ROWS - 1)


def random_col(board):
    """Return a random column."""
    return randint(0, COLUMNS - 1)


main()
