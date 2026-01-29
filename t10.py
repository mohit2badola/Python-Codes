# Write a program to check whether a number is a single-digit or multi-digit number.

x=int(input("Enter a number "))
num=str(x)
if len(num)>1:
    print("The number is not a single digit number")
elif len(num)==1:
    print("The number is a single digit number")
else:
    print("Invalid input")