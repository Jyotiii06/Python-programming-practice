a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=('+','-','*','/','%')
ch=input("Do you want do perform any operation?")

#if ch=='y' or ch=='Y':
  #  f=int(input("Enter operation you want to perform \n1- Addition +\n2- Subtraction -\n3- Multiplication *\n4-   /\n5- Modulus %\n"))
if ch=='n' or ch=='N':
    print("Thankyou Program ends")
elif ch=='y' or ch=='Y':
    f=int(input("Enter operation you want to perform \n1- Addition +\n2- Subtraction -\n3- Multiplication *\n4- Division /\n5- Modulus %\n"))
else:
    print("Invalid choice")
if f==1:
    print("Addition operator is performed ","\na =",a,"\nb =",b,"\nComputed result is",a+b)
elif f==2:
    print("Subtraction operator is performed ","\na =",a,"\nb =",b,"\nComputed result is",a-b)
elif f==3:
    print("Multiplication operator is performed ","\na =",a,"\nb =",b,"\nComputed result is",a*b)
elif f==4:
    if b!=0:
        print("Division operator is performed ","\na =",a,"\nb =",b,"\nComputed result is",a/b)
    else:
        print("Error !! Division by zero is not allowed")        
elif f==5:
    print("Modulus operator is performed ","\na =",a,"\nb =",b,"\nComputed result is",a%b)
else:
    print("Invalid oprator !!")
ch=input("\nDo you want do perform any other operation?")
if ch=='y' or ch=='Y':
    f=int(input("Enter operation you want to perform \n1- Addition +\n2- Subtraction -\n3- Multiplication *\n4- Division /\n5- Modulus %\n"))
elif ch=='n' or ch=='N':
    print("Thankyou Program ends")
else:
    print("Invalid choice!!")
