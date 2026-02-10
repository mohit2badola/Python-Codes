# Print pattern pyramid of numbers.

row=int(input("Enter the number of rows"))

for i in range(row):
    print(" "*(row-i-1)+"*"*(2*i+1))