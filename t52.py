# Create a number guessing game with limited attempts.
# let assume the maximum number of attempt to guess the nummber is 5
import random
max=5
lim=0
num=random.randint(1,100)

while lim<max:
    choice=int(input("Enter the number"))
    lim+=1
    if choice==num:
        print("You have entered the correct nummber GREAT GUESS")
        break
    elif choice>num:
        print("HINT: Number is less than the entered number")
    elif(choice<num):
        print("HINT: Number is greater than the entered number")
if lim==max:
    print("OUT OF ATTEMPTS WELL TRIED !!")
    print("The orignal number was",num)

        
