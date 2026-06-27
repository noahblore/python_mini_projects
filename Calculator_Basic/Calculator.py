print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))


if option in (1,2,3,4):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == 1:
        print(num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:    
        print("Invalid operation entered.")