#Ciclos while - Mientras
#adivina el numero

import random

def run():
    number_found = False 
    smallerNumber = int(input('Ingrese el numero mas pequeño: '))
    higherNumber = int(input('Ingrese el numero mas grande: '))
    print('Debes adivinar un numero entre {} y el {}'.format(higherNumber,smallerNumber))
    random_number = random.randint(smallerNumber,higherNumber)

    while not number_found:
        number = int(input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades!, encontraste el numero')
            number_found = True
        elif number > random_number:
            print('El numero es mas pequennio...')
        else:
            print('El numero es mas grande...')


if __name__ == '__main__':
    print('A D I V I N A  E L  N U M E R O . . . ')
    run()
