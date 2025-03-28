# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
# Check if last characters of the input match the suffix and then print the message.

user_input1 = input("Enter a text: ")
user_input2 = input("Enter the suffix: ")

suffix = len(user_input2)

if user_input1[-suffix:] == user_input2:
    print("The string ends with the given suffix.")
else:
    print("The string does not end with the given suffix.")

