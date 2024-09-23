"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
#a list with 4 elements and prints
my_list = ["Hydrogen","Helium","Lithium","Beryllium"]
print(my_list)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
#adding an element to the end of the list
my_list.append("Boron")
print(my_list)


"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
#removes hydrogen
my_list.remove("Hydrogen")
print(my_list)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
#replaces berylium with Nitrogen
my_list[2] = "Nitrogen"
print(my_list)


"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
#adds multiple items and prints
my_list.append("Carbon")
my_list.append("Oxygen")
my_list.append("Flourine")
my_list.append("Neon")
print(my_list)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
#delets index 0 or the first item
del my_list[0]
print(my_list)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

#creats a new list that is the first two items of my_list
# first_two = [my_list[0], my_list[1]]
first_two = my_list[0:2]
print(first_two)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
#cobines the first_two list and the my_list 
new_list = my_list + first_two
print(new_list)
