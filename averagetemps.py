#Calculadora de Temperaturas promedio ///Uso de Listas

def averageTemps(temps):
    sumTemps = 0
    for temp in temps:
        sumTemps += temp

    return sumTemps / len(temps)


if __name__ == '__main__':
    temps = [21,24,24,22,20,23,24]

    result = averageTemps(temps)

    print('La temperatura promedio es: {}'.format(result))
