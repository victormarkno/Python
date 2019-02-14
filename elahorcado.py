#Juego del Ahorcado

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
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def display_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- *')
    
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word,tries)
        current_letter = str(input('Escoge una letra: '))
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)
        if len(letter_indexes) == 0:
            tries+=1
            if tries == 7:
                display_board(hidden_word,tries)
                print('\n Perdiste!!!\n La palabra correcta era {}'.format(word))
                break
        else:
            for idx in letter_indexes:
               hidden_word[idx] = current_letter

            letter_indexes = []

            try:
               hidden_word.index('-')
            except ValueError:
                 print('\nFelicidades! Encontraste la palabra es: {}'.format(word))
                 break
            
           
if __name__ == '__main__':
    print('B I E N V E N I D O S  A L  J U E G O  D E L  A H O R C A D O')
    run()




    
