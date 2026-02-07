# Check if a number is a perfect number.

num=int(input("Enter a number"))
perfectnum=0
for i in range(1,num):
    if num%i==0:
        perfectnum+=i
if num==perfectnum:
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")
