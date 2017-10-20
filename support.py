# The support functions were forked from an MIT 6.0001 problem set. So no one sue me. Please.

import random
import string


def load_words(word_file):
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.

    :word_file: (str) Filename of word list
    """
    in_file = open(word_file, 'r')
    line = in_file.readline()
    wordlist = line.split()
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    word_guessed = True

    for letter in secret_word:
        if letter not in letters_guessed:
            word_guessed = False

    return word_guessed


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letter_count = len(secret_word)
    guessed_word_letters = ['_ ' for i in range(letter_count)]

    for i in range(letter_count):
        for letter in letters_guessed:
            if secret_word[i] == letter:
                guessed_word_letters[i] = letter

    guessed_word = ''
    for letter in guessed_word_letters:
        guessed_word = guessed_word + letter

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    alpha_list = []

    for letter in alphabet:
        if letter not in letters_guessed:
            alpha_list.append(letter)

    left_letters = ''
    for letter in alpha_list:
        left_letters = left_letters + letter

    return left_letters
