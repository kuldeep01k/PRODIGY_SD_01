def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Conversion Program")
    print("Supported units: Celsius (C), Fahrenheit (F), Kelvin (K)")
    
    # Prompt user for input
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the original unit of measurement (C, F, K): ").strip().upper()
    
    # Perform conversions based on the input unit
    if unit == "C":
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit == "F":
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit == "K":
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit entered. Please use C, F, or K.")
        return
    
    # Display the results
    print("\nConverted Temperatures:")
    print(f"Celsius: {celsius:.2f} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin: {kelvin:.2f} K")

if __name__ == "__main__":
    main()