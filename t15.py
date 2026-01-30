# Write a program to find the sum of first 10 natural numbers.

n=int(input("Enter the number to find the sum upto"))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of first ",n,"natural number is ",sum)