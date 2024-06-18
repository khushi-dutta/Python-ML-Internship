# Write a program that reads data from a CSV file and prints it to the console.

import csv

file_name = input("Enter the CSV file name: ")

try:

    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(", ".join(row))

except FileNotFoundError:
    print("Error: The file '" + file_name + "' was not found.")

except Exception as e:
    print("An error occurred: " + str(e))
