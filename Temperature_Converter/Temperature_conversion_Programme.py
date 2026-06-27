unit = input("Is this temperature in Celsius or Fahrenheit? (C/F) ")
temperature = float(input("What is the temperature? "))

if unit.upper() == "C":
    converted = (temperature * 9/5) + 32
    print(f"{temperature} degrees Celsius is equal to {converted} degrees Fahrenheit.")
elif unit.upper() == "F":
    converted = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is equal to {converted} degrees Celsius.")
else:
    print("Invalid unit entered.")