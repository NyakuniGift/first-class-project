from converter import celcius_to_fahrenheit, fahrenheit_to_celcius

print("Temperature Convertor")

print("1. Celcius to Fahrenheit")
print("2. Fahrenheit to Celcius")

choice = input("Choose a conversion (1 or 2)")

if choice == "1":
    try:
        celcius = float(input("Enter a temperature in Celcius: "))

        fahrenheit = celcius_to_fahrenheit(celcius)

        print(f"{celcius}°C is equal to {fahrenheit}°F")

    except ValueError:
        print("Invalid input. Please enter a number.")

elif choice == "2":
    try:
        fahrenheit = float(input("Enter a temperature in fahrenheit: "))

        celcius = fahrenheit_to_celcius(fahrenheit)

        print(f"{fahrenheit}°F is equal to {celcius}°C")

    except ValueError:
        print("Invalid input. Please enter a number.")

else :
    print("Invalid choice")