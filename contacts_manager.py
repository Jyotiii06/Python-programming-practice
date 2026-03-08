contacts={}
while True:
    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice=input("Enter choice:")
    if choice=="1":
        name=input("Enter name:")
        phone=int(input("Enter phone number:"))
        contacts[name]=phone
        print("Contact Added!")

    elif choice=="2":
        for name, phone in contacts.items():
            print(name,":",phone)

    elif choice=="3":
        name=input("Enter name to search:")
        if name in contacts:
            print("Phone:",contacts[name])
        else:
            print("Contact not found")

    elif choice=="4":
        name=input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice=="5":
        print("Byeee!!")
        
    else:
        print("Enter valid options!!")
        break        
