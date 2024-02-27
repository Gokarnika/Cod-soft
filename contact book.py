contact={}
def display_contact():
    print("name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1.Add new contact\n 2.Search contact\n 3. Display contact\n 4.update contact\n 5. Delete contact\n 6.Exit\n Enter your choice:"))
    if choice==1:
        name=input("Enter the contact name:")
        number=input("Enter the mobile number:")
        contact[name]=number
    elif choice==2:
        search_name=input("Enter the contact name:")
        if search_name in contact:
            print(search_name,"'s contact number is",contact[search_name])
        else:
            print("Name not found")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice==4:
        update_contact=("Enter the contact to be updated:")
        if update_contact in contact:
            number=input("enter phone nmber:")
            contact[update_contact]=number
            print("contact updated")
            display_contact()
        else:
            print("Name not found in contact book")
    elif choice==5:
        del_contact=input("Enter the contact need to be deleted:")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact yes/no?")
            if confirm=='yes' or confirm=='YES':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
            break
        
