import random
from words import words
import string


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():

    word = get_valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    while len(word_letters) > 0:
        print("You have used the letters: ", ' '.join(used_letters).upper())
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list).upper())
        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if (user_letter in word_letters):
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already guessed that letter")
        else:
            print('Invalid letter')


hangman()
