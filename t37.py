# Write a program to print ASCII value of a character.

ch=input("Enter a character ")

if len(ch)>1:
    print("The ASCII value of the first character",ch[0], "is ", ord(ch[0]))
else:
    print("The ASCII value of ",ch, "is ",ord(ch) )