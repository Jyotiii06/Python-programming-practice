import re
def check_password(password):
    score=0
    if len(password)>=8:
        score+=10
    if re.search("[a-z]",password):
        score+=1
    if re.search("[A-Z]",password):
        score+=1
    if re.search("[0-9]",password):
        score+=1
    if re.search("[!@#$%^&*]",password):
        score+=1
    if score<=2:
        print("Weak Password")
    elif score==3 or score==4:
        print("Medium Password")
    else:
        print("Strong Password")

password=input("Enter your password:")
check_password(password)
 
