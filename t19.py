# Write a program to find the factorial of a number.  

y=int(input("Enter a number to find its facorial"))
x=y
fact=1
while x>0:  
    fact*=x
    x=x-1
print("The facotrial of",y," is ",fact)