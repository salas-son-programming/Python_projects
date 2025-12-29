# Contact Book (CLI)
#o User can add, view, search, or delete contacts (name & phone).
#o Data stored in a list of tuples or dictionaries.
x = True
Contacts = []

while x:

    option = int(input("Tap 1 to add another contact, 2 to take a look at your contacts, tap 3 to search for a contact, tap 4 to delete a contact, tap 5 to quit: "))
    if option==1:
        print("ok")
        contact_name = input("Enter the name of your contact: ")
        contact_phone = int(input("enter the phone number: "))

        contact = (contact_name,contact_phone)
        Contacts.append(contact)
    elif option==2:
            for cont in Contacts:
                print(f"{cont[0]} : {cont[1]}")
    elif option==3:
        contact_searching = input("enter the name of the contact you are searching: ")
        for cont in Contacts:
            if contact_searching in cont:
                print(f"{cont[0]} : {cont[1]}")
    elif option == 4:
        contact_to_delete=input("enter the name of the contact you want to delete: ")
        for con in Contacts:
            if contact_to_delete in con:
                Contacts.remove(con)
    elif option == 5:
        x=False
    else :
        print("enter a number between the ones asked")


