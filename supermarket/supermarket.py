"""A program for the supermarket."""


def supermarket():
    """A program for the supermarket."""
    prices = {"banana": 4,
              "apple": 2,
              "orange": 1.5,
              "pear": 3}

    stock = {"banana": 6,
             "apple": 0,
             "orange": 32,
             "pear": 15}

    for item in prices:
        print (item)
        print ("price: {}".format(prices[item]))
        print ("stock: {}".format(stock[item]))
        print()


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


def print_evens():
    """Print out even numbers from a string."""
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for x in a:
        if(x % 2 == 0):
            print(x)


def fizz_count(x):
    """Count the number of times the word fizz occures in a list."""
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1

    return count


supermarket()
