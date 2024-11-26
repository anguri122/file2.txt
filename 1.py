def calculator():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    print('''
Choose an operation:
1 == Addition
2 == Subtraction
3 == Multiplication
4 == Division
    ''')
    
    def switch(value):
        if value == 1:
            return number1 + number2
        elif value == 2:
            return number1 - number2
        elif value == 3:
            return number1 * number2
        elif value == 4:
            if number2 != 0:  # Avoid division by zero
                return number1 / number2
            else:
                return "Error: Division by zero is undefined."
        else:
            return "Error: Invalid operation choice."
    
    try:
        c = switch(int(input("Enter your choice (1-4): ")))
        print("Result is:", c)
    except ValueError:
        print("Error: Please enter a valid number for the operation choice.")

calculator()

        
