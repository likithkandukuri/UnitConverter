print("\nWelcome to the Unit Converter\n")
def weight(value):
    while True:
        print("\nWeight / Mass Conversion")
        print("1. Kilograms → Pounds")
        print("2. Pounds → Kilograms")
        choice = input("Your choice: ")

        if choice == "1":
            result = value * 2.20462
            print(f"\n{value} kilograms = {result:.4f} pounds")
            return result
        elif choice == "2":
            result = value / 2.20462
            print(f"\n{value} pounds = {result:.4f} kilograms")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def distance(value):
    while True:
        print("\nDistance / Length Conversion")
        print("1. Kilometers → Miles")
        print("2. Miles → Kilometers")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 1.609
            print(f"\n{value} kilometers = {result:.4f} miles")
            return result
        elif choice == "2":
            result = value * 1.609
            print(f"\n{value} miles = {result:.4f} kilometers")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def temperature(value):
    while True:
        print("\nTemperature Conversion")
        print("1. Celsius → Fahrenheit")
        print("2. Fahrenheit → Celsius")
        choice = input("Your choice: ")

        if choice == "1":
            result = (value * 9/5) + 32
            print(f"\n{value}°C = {result:.4f}°F")
            return result
        elif choice == "2":
            result = (value - 32) * 5/9
            print(f"\n{value}°F = {result:.4f}°C")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def volume(value):
    while True:
        print("\nVolume Conversion")
        print("1. Liters → Gallons")
        print("2. Gallons → Liters")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 3.785
            print(f"\n{value} liters = {result:.4f} gallons")
            return result
        elif choice == "2":
            result = value * 3.785
            print(f"\n{value} gallons = {result:.4f} liters")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def speed(value):
    while True:
        print("\nSpeed Conversion")
        print("1. Kilometers per hour → Miles per hour")
        print("2. Miles per hour → Kilometers per hour")
        choice = input("Your choice: ")

        if choice == "1":
            result = value * 0.621371
            print(f"\n{value} kilometers/hour = {result:.4f} miles/hour")
            return result
        elif choice == "2":
            result = value / 0.621371
            print(f"\n{value} miles/hour = {result:.4f} kilometers/hour")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def area(value):
    while True:
        print("\nArea Conversion")
        print("1. Square meters → Square feet")
        print("2. Square feet → Square meters")
        choice = input("Your choice: ")

        if choice == "1":
            result = value * 10.764
            print(f"\n{value} square meters = {result:.4f} square feet")
            return result
        elif choice == "2":
            result = value / 10.764
            print(f"\n{value} square feet = {result:.4f} square meters")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def time(value):
    while True:
        print("\nTime Conversion")
        print("1. Seconds → Minutes")
        print("2. Seconds → Hours")
        print("3. Minutes → Seconds")
        print("4. Minutes → Hours")
        print("5. Hours → Seconds")
        print("6. Hours → Minutes")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 60
            print(f"\n{value} seconds = {result:.4f} minutes")
            return result
        elif choice == "2":
            result = value / 3600
            print(f"\n{value} seconds = {result:.4f} hours")
            return result
        elif choice == "3":
            result = value * 60
            print(f"\n{value} minutes = {result:.4f} seconds")
            return result
        elif choice == "4":
            result = value / 60
            print(f"\n{value} minutes = {result:.4f} hours")
            return result
        elif choice == "5":
            result = value * 3600
            print(f"\n{value} hours = {result:.4f} seconds")
            return result
        elif choice == "6":
            result = value * 60
            print(f"\n{value} hours = {result:.4f} minutes")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def pressure(value):
    while True:
        print("\nPressure Conversion")
        print("1. Pascals → PSI (Pounds per square inch)")
        print("2. PSI → Pascals")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 6895
            print(f"\n{value} pascals = {result:.4f} psi")
            return result
        elif choice == "2":
            result = value * 6895
            print(f"\n{value} psi = {result:.4f} pascals")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def energy(value):
    while True:
        print("\nEnergy Conversion")
        print("1. Joules → Calories")
        print("2. Calories → Joules")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 4184
            print(f"\n{value} joules = {result:.4f} calories")
            return result
        elif choice == "2":
            result = value * 4184
            print(f"\n{value} calories = {result:.4f} joules")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def data(value):
    while True:
        print("\nData Conversion")
        print("1. Bytes → Kilobytes")
        print("2. Bytes → Megabytes")
        print("3. Kilobytes → Bytes")
        print("4. Kilobytes → Megabytes")
        print("5. Megabytes → Bytes")
        print("6. Megabytes → Kilobytes")
        choice = input("Your choice: ")

        if choice == "1":
            result = value / 1000
            print(f"\n{value} bytes = {result:.4f} kilobytes")
            return result
        elif choice == "2":
            result = value / 1000000
            print(f"\n{value} bytes = {result:.4f} megabytes")
            return result
        elif choice == "3":
            result = value * 1000
            print(f"\n{value} kilobytes = {result:.4f} bytes")
            return result
        elif choice == "4":
            result = value / 1000
            print(f"\n{value} kilobytes = {result:.4f} megabytes")
            return result
        elif choice == "5":
            result = value * 1000000
            print(f"\n{value} megabytes = {result:.4f} bytes")
            return result
        elif choice == "6":
            result = value * 1000
            print(f"\n{value} megabytes = {result:.4f} kilobytes")
            return result
        else:
            print("Invalid choice! Please try again.\n")

def main():
    while True:
        try:
            number_input = float(input("Enter the starting number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    while True:
        print(f"\nCurrent Number: {number_input}")
        print("""
Functions: 
  1. Weight / Mass
  2. Distance / Length
  3. Temperature
  4. Volume
  5. Speed
  6. Area
  7. Time
  8. Pressure
  9. Energy
  10. Data / Digital Storage
  11. Exit
        """)

        user_input = input("Your choice: ")

        if user_input == "1":
            number_input = weight(number_input)
        elif user_input == "2":
            number_input = distance(number_input)
        elif user_input == "3":
            number_input = temperature(number_input)
        elif user_input == "4":
            number_input = volume(number_input)
        elif user_input == "5":
            number_input = speed(number_input)
        elif user_input == "6":
            number_input = area(number_input)
        elif user_input == "7":
            number_input = time(number_input)
        elif user_input == "8":
            number_input = pressure(number_input)
        elif user_input == "9":
            number_input = energy(number_input)
        elif user_input == "10":
            number_input = data(number_input)
        elif user_input == "11":
            print("\nThank you for using the Unit Converter! Goodbye.")
            break
        else:
            print("Invalid choice! Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
