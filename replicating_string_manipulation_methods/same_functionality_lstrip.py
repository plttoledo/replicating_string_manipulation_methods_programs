# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
# Use while and len

user_input = input("Enter a text: ")

i = 0
while i < len(user_input) and user_input[i] == ' ':
    i += 1

result = user_input[i:]
print(result)