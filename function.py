from converter import celcius_to_fahrenheit

print("Temperature Convertor")

try:
    celcius = float(input("Enter a temperature in Celcius: "))

    fahrenheit = celcius_to_fahrenheit(celcius)

    print(f"{celcius}°C is equal to {fahrenheit}°F")

except ValueError:
    print("Invalid input. Please enter a number.")