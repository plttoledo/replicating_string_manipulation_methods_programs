# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
# Import the string module, and then use the string.capwords() function

import string

user_input = input("Enter a text: ")

print(string.capwords(user_input))