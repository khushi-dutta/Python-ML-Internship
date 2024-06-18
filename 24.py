# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = number1 + number2
    print("The result of", number1, "+", number2, "is:", result)

elif operator == '-':
    result = number1 - number2
    print("The result of", number1, "-", number2, "is:", result)

elif operator == '*':
    result = number1 * number2
    print("The result of", number1, "*", number2, "is:", result)

elif operator == '/':
    
    if number2 != 0:
        result = number1 / number2
        print("The result of", number1, "/", number2, "is:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator. Please enter one of +, -, *, /.")
