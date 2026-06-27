
try:
    meal = float(input("Enter your meal amount: "))
    tip = float(input("Enter the tip percentage: ")) / 100
    tax = 0.06

    total_cost = meal + (meal * tip) + (meal * tax)
    print(f"\nYour meal was ${meal:.2f}, the tip was ${tip * meal:.2f}, with the additional tax being ${tax * meal:.2f}.")
    print(f"The total cost of the meal is: ${total_cost:.2f}\n")
except ValueError:
    print("Invalid input. Please enter valid numbers.")