import string

from words import words
import random as ran

def get_val(words):
    word = ran.choice(words)
    while '-' in word or ' ' in word:
        word = ran.choice(words)
    return word

def hangman():
    word = get_val(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input('Guess a letter').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if used_letters in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in user_letter:
        print('you have already used that letter')
    else: print('invalid letter, try agai.n')

user_input = input("type something:")
print(user_input)