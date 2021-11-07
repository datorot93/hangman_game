import os
import random

def read_file():
    words = []

    with open('./data/data.txt', 'r', encoding='utf_8') as file:        
        # for word in file:
        #     if word != '\n':
        #         words.append(word)
        words = [word for word in file if word != '\n']
    
    return words

def choose_word(words):
    word = random.choice(words)
    
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

    # word_dict = dict(map(lambda k, v: v = True if k == letter, word_dict))
    word_dict.update({ key: True for (key, value) in word_dict.items() if key == letter})

    return word_dict

def run():
    words = read_file()
    word = choose_word(words)
    word_dict = make_dict(word.strip())

    while False in list(word_dict.values()):
        letter = input('Please enter a letter: ')
        word_dict = set_letters(word_dict, letter)
        os.system('clear')     
        print_word(word_dict, word)


    # print(word_dict)


if __name__=='__main__':
    run()