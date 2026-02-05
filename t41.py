# Write a program to check whether a number is an Armstrong number.

# n=int(input("Enter a number to compute armstrong number"))
# armst=0
# l=len(str(n))
# for i in str(n):
#     armst+=(int(i)**l)
# if n==armst:
#     print("THE NUMBER IS AN ARMSTRONG NUMBER")
# else:
#     print("Thee number is not an armstrong number")



# program to print all Armstrong number between 1 to 1000

for n in range(1,1001):
    armst=0
    l=len(str(n))
    for i in str(n):
        armst+=(int(i)**l)
    if n==armst:
        print(n)
    