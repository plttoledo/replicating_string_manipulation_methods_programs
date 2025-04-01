# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
# Pretty much do the similar thing like in batch 6, just in reverse (and I mean by putting :- before len)

user_input1 = input("Enter a text: ")
user_input2 = input("Enter the suffix to remove: ")

if user_input1.endswith(user_input2):
    result = user_input1[:-len(user_input2)]
else:
    result = user_input1

print(result)