# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

user_input = input("Enter a text: ")

width = 20

print(user_input + " " * (width - len(user_input)))