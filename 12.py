#Write a python program that calculates the sum of the digits of a given number

number = input("Enter a number: ")

sum = 0

for digit in number:
    sum += int(digit)

print("The sum of the digits of the number is:", sum)
