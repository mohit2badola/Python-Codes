
d={}
def inserting(students,marks):
    for i in range(len(students)):
        d[students[i]]=marks[i]
    print("inserted")

def deleting(key,d):
    if key in d:
        del d[key]
        return "Deleted"
    else:
        return -1
    

def print_marks(key,d):
    if key in d:
        print(d[key])
    else:
        print("Key not present")
        

students=['Rohit','Vinay','Tarun','Subham']
marks=[60,80,50,90]

while True:
    print(d)
    choice=int(input("Enter 1 for inserting 2 for deleting 3 for viewing 0 for exit "))
    if choice==1:
        inserting(students,marks)

    elif choice==2:
        x=input("Rnter the name of the student whose entry you want to delete")
        deleting(x,d)
    
    elif choice==3:
        x=input("Rnter the name of the student whose entry you want to see")
        print_marks(x,d)
    
    elif choice==0:
        break

    else:
        print("Wrong choice!!!!!!!!!!!!!!!!!!")