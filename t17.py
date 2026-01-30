# Write a program to print the multiplication table of a number.

n=int(input("Enter the number whose table you want to print"))

for i in range(1,11):
    print(n,"X",i,"=",(n*i))