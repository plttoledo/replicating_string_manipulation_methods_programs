# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
# Use for loop, and then convert the lowercase into uppercase using ASCII. (lowercase letters have 32 values higher than uppercase letters, so -32), also needs to check if it has an uppercase, it shouldn't have to be converted

user_input = input("Enter a text: ")

for i in user_input:
    if i.islower():
        all_upper = chr(ord(i)-32)
    else:
        all_upper = i

    print(all_upper, end='')