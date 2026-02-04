# Write a program to display grades using if-elif-else.
# if marks are greater than 95 grade O
# if marks are greater than 85 and less than 95  grade A
# if marks are greater than 75 andf less than 75 grade B
# if marks are greater than 55 andf less than 75 grade C
# if marks are less than 55 grade F


marks = int(input("Enter the marks of the student "))
if marks>95:
    print("GRADE O")
elif marks<95 and marks >85:
    print("GRADE A")
elif marks<85 and marks >75:
    print("GRADE B")
elif marks<75 and marks >55:
    print("GRADE C ")
else:
    print("GRADE F")