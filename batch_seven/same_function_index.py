# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

user_input = input("Enter a text: ")
find_word = input("Enter the substring to find: ")

found_word = user_input.find(find_word)

print(found_word)