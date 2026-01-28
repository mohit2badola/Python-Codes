# Program to find the greatest of three number 

a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))

# condition
if(a>b and a>c):
   print("Number one is greatest among all three") 
elif(b>c and b>a):
    print("Number two is greatest among all three")
elif(c>a and c>a):
    print("Number three is greatest among all three")
else:
    print("All three are equal")