# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

user_input = input("Enter a text: ")
leading_zero = int(input("Enter how many leading zeros: "))

zero_padding = "0" * leading_zero + user_input

print(zero_padding)

