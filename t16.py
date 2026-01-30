# Write a program to find the sum of numbers entered by the user using a loop.
sum=0
n=int(input("Enter the number of numbers you want to take as input"))
for i in range(n):
    x=int(input("Enter the number "))
    sum+=x

print("The sum of the number is ", sum)