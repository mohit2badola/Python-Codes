# Write a program to reverse a number using a loop.

x=int(input("Enter a number to reverse it "))
y=x
rev=0
while y>0:
    mod=y%10
    rev=(rev*10)+mod
    y=y//10

print("The reverse of ",x,"is",rev) 