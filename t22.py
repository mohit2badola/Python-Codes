# Write a program to check whether a number is prime.

num=int(input("Enter a number"))

f=1

for i in range(1,num):
    if (num%i)==0:
        f+=1

if f==2:
    print("the number is prime")
else:
    print("the number is not prime")