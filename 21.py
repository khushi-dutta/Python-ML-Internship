# Write a python program that counts the occurrences of a specific element in a list.

elements = input("Enter a list of elements separated by spaces: ").split()

target = input("Enter the element to count: ")

occurrences = elements.count(target)

print("The element", target, "occurs", occurrences, "times in the list.")
