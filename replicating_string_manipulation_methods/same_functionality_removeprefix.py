# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
# Use startswith

user_input1 = input("Enter a text: ")
user_input2 = input("Enter the prefix to remove: ")

if user_input1.startswith(user_input2):
    result = user_input1[len(user_input2):]
else:
    result = user_input1

print(result)
