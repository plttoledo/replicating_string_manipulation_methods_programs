# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
# For loop if upper, return lower, vice versa

string = input("Enter a text: ")
new_string = ""

for i in string:
    if i.isupper():
        new_string += i.lower()
    else:
        new_string += i.upper()
print(new_string)