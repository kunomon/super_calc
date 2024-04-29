from calc import Calc

def main():
  app = Calc()

  print('Super Calc 2.0')
  print('Selecione uma opção:')
  print('[1]: Convert Celsius to Fahrenheit')
  print('[2]: Convert Fahrenheit to Celsius')
  print('[3]: Convert Pound to KG')
  print('[4]: Convert KG to Pound')

  option = input('...:')

  if option == '1':
    celsius = int(input())
    fahren = app.tempCalc.celsiusToFahrenheit(celsius)
    print('Resultado da convers]ao: ', fahren)
  elif option == 2:
    fahren = input()
    app.tempCalc.fahrenheitToCelsius(fahren)
  elif option == 3:
    pound = input()
    app.massCalc.poundToKg(pound)
  else:
    # Exec convert KG to Pound
    print()

main()