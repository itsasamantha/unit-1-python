# creates the list the todos is stored in
todo_list = []


#infinite while loop
while True:
    #prints out the current list
    print("------------------------------------------------------------------")
    print()
    print("Your current todo list:")
    # the number showed in the list print out
    num = 1
    #checks to see if there is something in the list
    if todo_list == []:
        #spacing
        print()
        print()
        print("There is nothing in your list right now")
    else:
        # print out each item on its own line
        for i in todo_list:
            print(f"{num}) {i}")
            num+=1
    #spacing
    print()
    print()
    # asking the user to add or remove
    decision = input("Would you like to add, remove, clear all  or edit your to do list? ")
    if decision == "add":
        #spacing
        print()
        print()
        action = input("What is it that you would like to add to your todo list? ")
        #makes suure there was an input
        if action.strip() == "":
            print()
            print()
            print("Please write a task to add")
            #spacing
            print()
            print()
        else:
            # adds the writren item to the list 
            todo_list.append(action)
            #spacing
            print()
            print()
    elif decision == "remove":
        #checks to see if there is something in the list
        if todo_list == []:
            #spacing
            print()
            print()
            print("There is nothing in your list right now")
        else:
            #spacing
            print()
            print()
            # removes based on the item not the number
            action = input("Which todo item needs to be removed? ")
            todo_list.remove(action)
            #spacing
            print()
            print()
            
    elif decision == "clear all":
        #checks to see if there is something in the list
        if todo_list == []:
            #spacing
            print()
            print()
            print("There is nothing in your list right now")
        else:
            #goes through and removes every item
            for x in todo_list:
                print()
                print()
                todo_list.remove(x)
                print()
                print()
    elif decision == "edit":
        #checks to see if there is something in the list
        if todo_list == []:
            #spacing
            print()
            print()
            print("There is nothing in your list right now")
        else:
            #asks for the number (using the list of what should be added)
            edit_num = int(input("Which item would you like to edit? (Please use a number)"))
            print()
            print()
            change = input("What ould you like to change it to? ")
            print()
            print()
            #changes that list item to the new value change
            todo_list[edit_num-1] = change
    else:
        #spacing
        print()
        print()
        print("Sorry I didn't get that could you please us the exact woring of the question.")
        print("Please type add, remove, clear all or edit")
        #spacing
        print()
        print()
        

