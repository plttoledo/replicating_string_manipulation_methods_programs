# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

user_input = input("Enter a text: ")
find_word = input("Enter the substring to find: ")

found_word = user_input.rfind(find_word)

print(found_word)