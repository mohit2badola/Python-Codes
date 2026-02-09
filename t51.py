# Find GCD of two numbers using a loop.

num1=int(input("Enter a number 1"))
num2=int(input("Enter a number 2"))
small=0
GCD=0
if num1<num2:
    small=num1
else:
    small=num2
for i in range(1,small+1):
    
    if num1%i==0 and num2%i==0:
        GCD=i
print(f"The GCD is {GCD}")