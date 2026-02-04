# Write a program to reverse a string using a loop.

str=input("Enter a string to reverse")
revstr=""


# for i in str:
#     revstr=i+revstr
# print("The string after revering is ", revstr)


revstr=str[::-1]
print("Reversed", revstr)