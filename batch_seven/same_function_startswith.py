# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

user_input1 = input("Enter a text: ")
user_input2 = input("Enter the prefix: ")

prefix = len(user_input2)

if user_input1[:prefix] == user_input2:
    print("The string starts with the given prefix.")
else:
    print("The string does not start with the given prefix.")