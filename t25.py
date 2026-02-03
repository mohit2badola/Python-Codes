# Write a program to find the largest digit in a number.

num=int(input("Enter a number"))
snum=str(num)
large=int(snum[0])
for i in snum:
    if int(i)>large:
        large=int(i)

print("The largest number in a digit is", large)