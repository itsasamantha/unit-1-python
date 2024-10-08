#creates an empty dictionary
phonebook = dict()
#infinate loop
while True:
    print("----------------------------")
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")
    print()

    #users choice
    choice = input("Enter your choice: ")

    if choice  == "1":
        print()
        name = input("Enter your contacts name: ")
        print()
        phone_num = input("Enter your contacts number:")
        #makes sure there are ten characters
        if len(phone_num) != 10:
            print("Please enter a 10 digit number")
        else:
            # for x in phone_num:
            #     if x != 1:
            #         print() way too long
            #adds a new key and value pair  
            phonebook[name] = phone_num
            print()
    if choice == "2":
        print()
        deletion = input("Enter the name of the contact you want to delete: ")
        #deletes based on the key or name
        del phonebook[deletion]
        print()
        print("Contact deleted successfully!")
        print()
    if choice == "3":
        print()
        for x in phonebook:
            print(f"{x}: {phonebook[x]}")
            print()
    if choice != 1 or choice != 2 or choice!= 3 or choice != 4:
        print()
        print("Please enter the number for one of the choices! ")
        print()
    if choice == "4":
        break

