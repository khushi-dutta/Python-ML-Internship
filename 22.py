# Write a python program that returns the minimum and maximum values in a list of numbers.

numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

min_value = min(numbers)
max_value = max(numbers)

print("The minimum value in the list is:", min_value)
print("The maximum value in the list is:", max_value)
