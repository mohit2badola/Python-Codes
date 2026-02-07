# Simulate ATM menu (withdraw, deposit, check balance) using loops and conditions.
balance=646564
print("Enter 'w' for withdrew\n'd' for deposit\n 'b' for balance enquiry ")
choice=input("Enter your choice")
if choice=='d' or choice=='D':
    addon=int(input("Enter the amount of money you want to deposit"))
    balance+=addon
    print(f"BALANCE : {balance}")

elif(choice=='w' or choice=='W'):
    remove=int(input("Enter the amount you want to withdrew"))
    if balance>=remove:
        balance=balance-remove
        print(f"BALANCE : {balance}")
    else:
        print("INSUFFICIENT BALANCE")

elif (choice=='B' or choice=='b'):
    print(f"BALANCE : {balance}")

else:
    print("WARNING : WRONG OPTION")
