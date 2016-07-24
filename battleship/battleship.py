"""Battleship game."""

from random import randint


def main():
    """Battleship game."""
    board = []

    for i in range(5):
        board.append(["O"] * 5)

    ship_row = random_row(board)
    ship_col = random_col(board)

    for turn in range(1, 5):
        print('\n\n')
        print('Guess #{} out of 4'.format(turn))
        print('=' * 20)
        print_board(board)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if (guess_row == ship_row and guess_col == ship_col):
            print ("Congratulations! You sank my battleship!")
            break
        else:
            if (guess_row >= len(board) or guess_col >= len(board)):
                print("Oops, that's not even in the ocean.")
            elif (board[guess_row][guess_col] == 'X'):
                print("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = 'X'
                if turn >= 4:
                    print("Game Over.")


def print_board(board):
    """Print the game grid."""
    for row in board:
        print (" ".join(row))


def random_row(board):
    """Return a random row."""
    return randint(0, len(board) - 1)


def random_col(board):
    """Return a random column."""
    return randint(0, len(board) - 1)


main()
