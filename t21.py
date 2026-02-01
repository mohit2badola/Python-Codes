# Write a program to check whether a number is a palindrome.

num=int(input("Enter a number to check for palindrome"))

cnum=num
palin=0
while num>0:
    mod=num%10
    palin=(palin*10)+mod
    num=num//10
if palin==cnum:
    print("the number is palindrome")
else:
    print("The number is not palindrome")