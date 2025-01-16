FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temperature = input('Enter the temperature to convert:')
if str.isdigit(temperature):
    temperature = int(temperature)
    is_celsius_or_fahrenheit = input('Is this temperature in Celsius or Fahrenheit? (C/F):').lower()


    if is_celsius_or_fahrenheit == 'c':
        print(temperature,'°C' ,'is', convert_to_fahrenheit(temperature),'°F')
    elif is_celsius_or_fahrenheit == 'f':
        print(temperature, '°F', 'is', convert_to_celsius(temperature),'°C')
    else:
        print('invalid input')
else:
        print('Invalid temperature. Please enter a numeric value.')

