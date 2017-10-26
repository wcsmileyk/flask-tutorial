from support import get_available_letters, get_guessed_word, is_word_guessed, load_words, choose_word
from gallows import gallow_pic


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * X At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * X The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letter_count = len(secret_word)
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    guesses = 6

    print('Secret word has %s letters' & letter_count)
    print('*' * 10)

    playing = True

    while playing:
        available_letters = get_available_letters(letters_guessed)
        print('You have %s guesses left' % guesses)
        print('Available letters: %s' % available_letters)
        print(gallow_pic[6 - guesses])
        print(guessed_word)

        guess = input('Please guess a letter: ').lower()
        need_guess = True

        while need_guess:
            if guess.isalpha() and len(guess) == 1 and guess in available_letters:
                need_guess = False
            if len(guess) != 1:
                guess = input('Sorry, guess exactly 1 letter: ').lower()
                continue
            if not guess.isalpha():
                guess = input('Sorry, only guess letters: ').lower()
                continue
            if guess not in available_letters:
                guess = input('Sorry, you already guessed that. Guess again: ').lower()
                continue

        letters_guessed.append(guess)

        if guess not in secret_word:
            guesses -= 1
            print('Sorry, no %s in word' % guess)
        else:
            print('Good guess!')
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if is_word_guessed(secret_word, letters_guessed):
            print('You win!')
            print(guessed_word)
            playing = False

        if guesses == 0:
            print(gallow_pic[6 - guesses])
            print(guessed_word)
            print('You lose!')
            print('The secret word was: ', secret_word)
            playing = False


if __name__ == "__main__":
    wordlist = load_words('words.txt')
    secret_word = choose_word(wordlist)
    hangman(secret_word)
