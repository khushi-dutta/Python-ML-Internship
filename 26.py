# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

input_string = input("Enter a string: ")

prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

start = input_string.startswith(prefix)
end = input_string.endswith(suffix)

print("The string '" + input_string + "' starts with the prefix '" + prefix + "'.", start)
print("The string '" + input_string + "' ends with the suffix '" + suffix + "'.", end)
