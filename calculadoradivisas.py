# Calculadora de Divisas, Pesos Argentinos $Ars => $USD
def foreign_exchange_calculator(ammount):
      usd_to_ars = 27.9 #Tipo de Cambio 27/07/2018
      return round(ammount / usd_to_ars,3)
def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos argentinos a dolares')
    print('')

    ammount = float(input('Ingrese la cantidad de pesos argentinos a dolares: '))
    result = foreign_exchange_calculator(ammount)

    print('${} pesos argentinos equivalen a ${} dolares americanos'.format(ammount,result))

if __name__ == '__main__':
    run()
