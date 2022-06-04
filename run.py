import random
# Import The Module for the game
from words import wordList


def getWord():
    """Selects the word for the round"""
    word = random.choice(wordList)
    return word.upper()

# def play(word):
#     """Function to guess the word"""
#     wordCompletion = "_" * len(word)
#     guess = False
#     guessedLetters = []
#     guessedWords = []
#     tries = 6
#     print("Get ready to save someone's life!")
    

def hangman():
    stages = [
        # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages


def main():
    word  = getWord()
    play(word)
    while input("Play again? (Y/N) ").upper|() == "Y":
        word = getWord()
        play(word)

