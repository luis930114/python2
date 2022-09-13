# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_word(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---* ---* ---* ---* ---* ---* ---* ---*')

def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_word(hidden_word,tries)
        current_letter = str(raw_input('Escoge una letra: '))
        letter_indexes = []

        for idx in range(len(word)):
            if word[idx] == current_letter :
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7 :
                display_word(hidden_word, tries)
                print('')
                print('LO SENTIMOS, PERDISTE. LA PALABRA ERA {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('!FELICIDADES GANASTE¡ LA PALABRA ES {}'.format(word))
            break

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
