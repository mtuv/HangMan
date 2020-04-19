import string
import random


def create_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def input_check():
    user_input = input("Please choose an amount of letters you want to play with.\n")

    while True:
        try:
            val = int(user_input)
            return val

        except ValueError:
            try:
                val = float(user_input)
                print("That " + str(val) + " is a float  number. Please input a string ")
            except ValueError:
                print("That's not even a number at all.")


def hangman():

    print("This is a game of Hang Man. Each 'word' is made up of random lowercase letters.")

    word_count = input_check()

    created_word = create_random_string(word_count)

    i = 0

    while i < word_count:
        player_guess = str(input("Type in your guess as a single lowercase letter.\n"))

        if created_word[i] == player_guess:
            print("You got it right! The letter really is " + str(player_guess))
            i += 1
            continue

        else:
            print("You didn't get it right. Please try again.")

    print("Congratulations! You correctly guessed the word " + created_word + ". I bet it took a while.")


hangman()
