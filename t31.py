# Write a program to check whether a number is divisible by both 3 and 7.

x=int(input("Enter a number"))
if x%7==0 and x%3==0:
    print("The number is divisible by both")
elif x%7==0:
    print("The number is divisible by 7 only")
elif x%3==0:
    print("The number is divisible by 3 only")
else:
    print("The number is not divisible by both")