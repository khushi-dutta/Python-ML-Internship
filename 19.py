# Write a python program that removes all punctuation from a given string.

import string

def remove_punctuation(input_string):

    translator = str.maketrans('', '', string.punctuation)
    
    clean_string = input_string.translate(translator)
    
    return clean_string

input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)

print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
