# Write a program to display menu-based calculator using if-else.

num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

choice=input("Enter your choice \n+ for addition\n- for subraction\n* for multiplication\n/ for division")

if choice=="+":
    print(f"Sum is {num1+num2}")
elif choice=="-":
    print(f"The ssubraction is {num1-num2}")
elif choice=="*":
    print(f"The multiplication is {num1*num2}")
elif choice=="/":
    if num2!=0:
        print(f"The division is {num1/num2}")
    else:
        print("Division by 0 not possible")
else:
    print("WRONG CHOICE!")