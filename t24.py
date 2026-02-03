# Write a program to find the sum of digits of a number.

num=int(input("Enter a number"))

cnum=str(num)
sum=0
for i in cnum:
    sum+=int(i)

print("The sum is",sum)