# Write a program to find the smallest of three numbers.

num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))

if (num1==num2) and (num2==num3):
    print("All three numbers are equal")
elif (num1>num2):
    if num1>num3:
        print("Num 1 is greatest of all")
    else:
        print("Num3 is gratest of all")
elif(num2>num3):
    print("Num2 is greatest of all")
else:
    print("Num 3 is greatest of all")