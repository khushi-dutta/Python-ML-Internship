# Write a python program that checks if two strings are anagrams of each other.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

are_anagrams = sorted(string1) == sorted(string2)

if are_anagrams:
    print("The strings are anagrams.")
    
else:
    print("The strings are not anagrams.")
