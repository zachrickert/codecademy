"""This is a Pig Latin Translator."""

"""Pig Latin is a language game, where the first letter of the word is moved to
 the end and add "ay."
So "Python" becomes "ythonpay."
Here are the steps to write a Pig Latin translator in Python:

* Ask the user to input a word in English.
* Make sure the user entered a valid word.
* Convert the word from English to Pig Latin.
* Display the translation result.
"""


def main():
    """The pig latin translator."""
    print ('Welcome to the Pig Latin Translator!')
    original = input("Enter a word: ")

    pyg = "ay"

    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
    else:
        print ("empty")


main()
