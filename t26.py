# Write a program to print Fibonacci series up to n terms.

n=int(input("Enter the length of fibonacci series"))
sto1=0
sto2=1
for i in range(n):
    sum=sto1+sto2
    sto1=sto2
    sto2=sum
    print(sum)

