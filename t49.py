# Keep taking input until user enters a prime number.
a=True
while a:
    ct=0
    x=int(input("Enter a number"))
    for i in range(1,x):
        if x%i==0:
            ct+=1
        
    if ct==1:
        a=False
    else:
        pass