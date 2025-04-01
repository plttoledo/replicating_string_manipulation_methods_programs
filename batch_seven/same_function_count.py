# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

user_input = input("Enter a text: ")
counting = input("What will you count in the text?: ")

count = 0

for i in user_input:
    if i == counting:
        count += 1

print(count)