# Write a program that copies the contents of one text file to another.

source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

with open(source_file, 'r') as src:
    content = src.read()

with open(destination_file, 'w') as dst:
    dst.write(content)

print("Contents copied from", source_file, "to", destination_file)
