# use the random module
import random
# Words collected for game
from words import word_list


def get_word():
    """Selects the word from words module for the current round"""
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """Guess the word for the current round"""
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    # Start Screen
    print("Let's play Hangman!")
    print("===================")
    print(display_hangman(tries))
    print("===================")
    print(word_completion)
    print("RULES OF THE GAME!!")
    print("1) The Game starts NOW, Press a letter you think the word contains")
    print("2) You have 6 attempts to guess the word right")
    print("3) Each wrong guess means hangman is losing health!")
    print("4) If you fail to win, hangman dies!!")
    print("Let's see if you're a hero or not!")
    print("*********************************")
    print("GOOD LUCK!")
    print("*********************************")
    print("\n")

    # While The game is running
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: \n").upper()
        if len(guess) == 1 and guess.isalpha():
            # Repeating your choice
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                # If the choice is incorrect minus your tries
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i,
                    letter in enumerate(word)
                    if letter == guess
                    ]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")

        # The end of the round displays here
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    # If you guess the word right
    if guessed:
        print("Congrats, you guessed the word! You win!")
    # When the user loses the round
    else:
        print("You ran out of tries. The word was " + word + ".")


def display_hangman(tries):
    """Displays the hangman per guess as you play"""
    stages = [  # final state: head, torso, both arms, and both legs
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
    return stages[tries]


def main():
    """The main app function"""
    word = get_word()
    play(word)
    # Choose to reply the game or exit the application
    while input("Play Again? (Y/N) \n").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
