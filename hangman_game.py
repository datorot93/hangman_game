# Hangman
from hangman_art import HANGMANPICS

# Utilities
import os
import random
import re



def read_file():
    try:
        words = []
        with open('./files/data.txt', 'r', encoding='utf_8') as file:
            words = [word for word in file if word != '\n']
    except FileNotFoundError:
        print('There is not exists a data file with the words')
        exit()
    return words    

def choose_word(words):
    try:
        word = random.choice(words)
    except IndexError:
        print('The data file does not contain any word. Please ensure that it is not empty.')
        exit()
    return word

def make_dict(word):
    word_dict = {key:False for key in word}

    return word_dict

def print_word(word_dict, word):
    word = word.strip()
    for letter in word:
        if word_dict[letter] == False:
            print('_', end=' ')
        else:
            print(letter, end=' ')

def set_letters(word_dict, letter):
    """ Function to  update the letters """
    word_dict.update({ key: True for (key, value) in word_dict.items() if key == letter})

    return word_dict

def is_letter(letter):
    if re.search('[a-zA-Z]', letter):
        return True
    return False

def run():
    errors = 0

    words = read_file()
    word = choose_word(words)
    word_dict = make_dict(word.strip())
    os.system('clear')  
    print_word(word_dict, word)

    while False in list(word_dict.values()) and errors < len(HANGMANPICS):
        print()
        print(word_dict)
        print('Errors: {}'.format(errors))
        letter = input('Please enter a letter: ')
        if not is_letter(letter) or len(letter) > 1:
            os.system('clear')  
            print_word(word_dict, word)
            print('Your input have to be ONE letter, it can not be a number or a text with more than 1 character')
            continue

        word_dict = set_letters(word_dict, letter)
        if letter not in word:
            os.system('clear')
            print(HANGMANPICS[errors])
            print_word(word_dict, word)
            errors+=1
        else:
            os.system('clear')
            if errors != 0:
                print(HANGMANPICS[errors])
            print_word(word_dict, word)

    if errors < len(HANGMANPICS):
        os.system('clear')
        print('#' * 20)
        print('CONGRATULATIONS, YOU WON!!!')
        print('#' * 20)


if __name__=='__main__':
    run()