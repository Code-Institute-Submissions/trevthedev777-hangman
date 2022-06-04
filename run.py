import random
# Import The Module for the game
from words import word_list


def get_word():
    """Selects the word for the round"""
    word = random.choice(word_list)
    return word.upper()


