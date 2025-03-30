# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

user_input = input("Enter a text: ")
result = ""

for letters in range(len(user_input)):
    if letters == 0:
        result += user_input[letters].upper()
    else:
        result += user_input[letters].lower()

print(result)
