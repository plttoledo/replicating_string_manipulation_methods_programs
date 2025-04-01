# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
# Same stuff in batch 6, just reverse it

string = input("Enter a text: ")

lowercases = True
for char in string:
    if 'A' <= char <= 'Z':
        lowercases = False
        break

if lowercases:
    print("The text is in all lowercase letters.")
else:
    print("The text is not in all lowercase letters.")