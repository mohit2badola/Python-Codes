# Write a program to calculate the sum of squares of first n numbers.

n=int(input("Enter a number"))
sum=0
for i in range(1,n+1):
    sqr=i*i
    sum+=sqr
print(f"The square of first {n} number is{sum}")