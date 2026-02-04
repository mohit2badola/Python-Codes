# Write a program to find the sum of even and odd numbers separately.

x=int(input("Enter a number"))
cn=str(x)
esum=0
osum=0
for i in cn:
    if int(i)%2==0:
        esum+=int(i)
    else:
        osum+=int(i)

print("The sum of even number are",esum)
print("The sum of odd number are",osum)