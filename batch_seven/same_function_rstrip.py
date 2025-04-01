# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rsplit() function.

user_input = input("Enter a text: ")

i = len(user_input) - 1
while i >= 0 and user_input[i] == ' ':
    i -= 1

result = user_input[:i + 1]
print(result)