# Program to check the marks of a student

sub1=int(input("Enter the marks of student in subject 1 "))
sub2=int(input("Enter the marks of student in subject 2 "))
sub3=int(input("Enter the marks of student in subject 3 "))
sub4=int(input("Enter the marks of student in subject 4 "))
sub5=int(input("Enter the marks of student in subject 5 "))

total_marks=sub1+sub2+sub3+sub4+sub5
percent=(total_marks*33)/100

if percent>=165:
    
    print("The student has pass the subjects")
else: 
    print("The student has not pass the subjects")