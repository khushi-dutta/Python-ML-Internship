# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines = []

print("Enter multiple lines of input. Press Enter without typing anything to finish.")

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

print("Lines entered:")

for line in lines:
    print(line)
