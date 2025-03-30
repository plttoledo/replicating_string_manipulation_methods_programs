# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

user_input= input("Enter a text: ")
width = 50
spaces = (width - len(user_input)) // 2

print(" " * spaces + user_input + " " * spaces)