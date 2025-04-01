# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
# lmao not done

user_input = input("Enter a text: ")

width = 50

print(" " * (width - len(user_input)) + user_input)