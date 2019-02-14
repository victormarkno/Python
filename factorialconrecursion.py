#Factorial de un numero, usar recursividad.

def factorial(number):
    if number == 0:
        return 1
    
    return number * factorial(number - 1)


if __name__ == '__main__':
    number = int(input('Ingrese numero a convertir en factorial: '))
    result = factorial(number)
    print('El resultado es: {}'.format(result))

    
