#Cacular si un numero es primo o no
import math

def is_prime(number):
    if (number < 2):
        return False
    else:
        divisor = int(math.sqrt(number))
        for i in range(2,divisor+1):
            if (number % i) == 0:
                return False
        return True
            
                
def run():
    number = int(input('Escribe un numero: '))
    result = is_prime(number)
    if result is True:
        print('El Numero {} es primo'.format(number))
    else:
        print('El Numero {} no es primo'.format(number))


if __name__ == '__main__':
    run()
