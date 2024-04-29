class TempCalc:    
  def celsiusToFahrenheit(self, celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
  
  def fahrenheitToCelsius(self, fahren):
    celsius = (fahren - 32) * 9/5
    return celsius