#Multiplos de 3 hasta un numero ingresado por el usuario ahora usando recursividad

def multiplos(number):
    if number == 3:
        return print('el Numero {} es multiplo de 3'.format(number))
    if number % 3 == 0:
        print('el Numero {} es multiplo de 3'.format(number))
    return multiplos(number - 1)


if __name__ == '__main__':
    print('Multiplos de 3 hasta un numero determinado...')
    number = int(input('Ingrese un numero: '))
    multiplos(number)
                 
