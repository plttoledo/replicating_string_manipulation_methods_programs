# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
# Use for loop

string = input("Enter a text: ")

uppercases = True
for char in string:
    if 'a' <= char <= 'z':
        uppercases = False
        break

if uppercases:
    print("The text is in all uppercase letters.")
else:
    print("The text is not in all uppercase letters.")