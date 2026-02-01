# Write a program to print all prime numbers between 1 and 100.

f=0
for i in range(1,101):
    for j in range(1,i):
        if i%j==0:
            f+=1
    if f==1:
        print(i)

    f=0
