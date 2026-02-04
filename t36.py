# Write a program to check whether a string is a palindrome.

str=input("Enter a string")
str=str.upper()
revstr=str[::-1]
if str==revstr:
    print("The string is palindrome")
else:
    print("The string is not palindrome")