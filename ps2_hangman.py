# CS 111 Problem Set 3
# Hangman
# Alan Weng / Zeyu Weng
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):

    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
choosen_word = str(choose_word(wordlist))
userGuess = ''


def main():
    print(choosen_word)
    print('Welcome to the game, Hangman!\n'
          f'I am thinking of a word that is {len(choosen_word)} letters long.')
    output()


def output():

    avaliable_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    converted_letters = avaliable_letters.split(' ')

    Guesses = int(len(choosen_word) * 1.5)
    under_score = []

    for i in range(len(choosen_word)):
        under_score.append('_')


    while(Guesses > 0):
        print('')
        print('------------\n'
            f'You have {Guesses} guesses left.\n'
            'Available letters: ',end='')

        for i in converted_letters:
                print(i, end='')
        
        print()
            

        userGuess = input('Please guess a letter: ')
        lower_user_guess = userGuess.lower()
        placement = ([pos for pos, char in enumerate(choosen_word) if char == lower_user_guess])
        temp = ''

        if placement == []:
            converted_letters.remove(lower_user_guess)
            for i in converted_letters:
                print(i, end='')
            print()
            print('Oops! That letter is not in my word: ',end='')
            for i in under_score:
                print(i, end='')

        elif bool(placement):
            converted_letters.remove(lower_user_guess)
            for i in converted_letters:
                print(i, end='')
            print()
            for element in placement:
                under_score[element] = lower_user_guess
            print('Good guess: ',end='')
            for i in under_score:
                print(i, end='')

        if temp.join(under_score) == choosen_word:
            print('')
            print('Congratulations! You won!')
            break

        print('')
        
        Guesses -= 1
    
    if Guesses == 0:
        print()
        print('YOU LOST')
        print('Sorry but you ran out of guesses!')

main()