"""A program for the supermarket."""


def names():
    """Function to loop through a series of names."""
    names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

    for name in names:
        print(name)


def dictionary():
    """Print out excerpts from the dictionary."""
    webster = {"Aardvark": "A star of a popular children's cartoon show.",
               "Baa": "The sound a goat makes.",
               "Carpet": "Goes on the floor.",
               "Dab": "A small amount."}

    for entry in webster:
        print (webster[entry])

dictionary()
