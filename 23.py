# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

choice = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit.")


elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    celsius = (fahrenheit - 32) * 5/9

    print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius.")


else:
    print("Invalid input. Please enter 'C' or 'F'.")
