# Write a program to print all factors of a number.


num=int(input("Enter anumber"))
for i in range(1,num+1):
    if num%i==0:
        print(i)