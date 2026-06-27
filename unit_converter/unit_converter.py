print("\n ** Unit Converter **\n")

conversion_available = [ (1, "km", "miles"),
                         (2, "miles", "km"), 
                         (3, "kg", "pounds"),
                         (4, "pounds", "kg"),
                         (5, "Celsius", "Fahrenheit"),
                         (6, "Fahrenheit", "Celsius")
]
                        
print("\nAvailable conversions: \n ")

for conversion, from_unit, to_unit in conversion_available:
    print(f"{conversion}. {from_unit} to {to_unit}")
try:
    conversion = input("\nEnter the number of the conversion you want to perform: ")
    conversion_index = int(conversion) - 1

    conversion_number, from_unit, to_unit = conversion_available[conversion_index]
except (ValueError):
    print("\nInvalid input. Please enter a number corresponding to the conversion.\n")
    exit()

from_value = float(input(f"\nEnter the value in {from_unit}> "))
if conversion_number == 1:
    to_value = from_value * 0.62
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
elif conversion_number == 2:
    to_value = from_value / 0.62
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
elif conversion_number == 3:
    to_value = from_value * 2.20462
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
elif conversion_number == 4:
    to_value = from_value / 2.20462
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
elif conversion_number == 5:
    to_value = (from_value * 9/5) + 32
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
elif conversion_number == 6:
    to_value = (from_value - 32) * 5/9
    print(f"\n{from_value} {from_unit} is equal to {to_value} {to_unit}")
