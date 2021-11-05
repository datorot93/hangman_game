import os
import random

def read_file():
    words = []

    with open('./archivos/data.txt', 'r', encoding='utf_8') as file:        
        for word in file:
            if word != '\n':
                words.append(word)
    
    return words

def choose_word(words):
    word = random.choice(words)
    
    return word

def make_dict(word):
    word_dict = {key:False for key in word}

    return word_dict

def print_word(word_dict):

    for key, value in word_dict.items():
        if value == False:
            print('_', end=' ')
        else:
            print(key, end='')

def run():
    words = read_file()
    word = choose_word(words)
    word_dict = make_dict(word.strip())
    print_word(word_dict)

    # print(word_dict)


if __name__=='__main__':
    run()