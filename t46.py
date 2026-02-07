#  Find all numbers between 1–500 divisible by 7 but not by 5.

for i in range(1,501):
    if (i%7==0) and (i%5!=0):
        print(i)