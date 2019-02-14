#Multiplos de 3 hasta un numero ingresado por el usuario

def multiplos(number):
    for i in range(number):
        if i % 3 == 0:
            print(i)


if __name__ == '__main__':
    print('Multiplos de 3 hasta un numero determinado...')
    number = int(input('Ingrese un numero: '))
    multiplos(number)
                 
