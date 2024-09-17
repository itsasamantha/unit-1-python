"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
my_float = 90.5
# printing the original float
print(my_float)
#converting and printitng to int
my_not_float = int(my_float)
print(my_not_float)




"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
# creating a var that takes user input
user_number = int(input("Type any number"))
#checking if num is 0 positive or negative
# and prints
if user_number == 0:
    print("This number is Zero")
elif user_number < 0:
    print("This number is negative")
else:
    print("This number is positive")
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
# creating the inputed int and float
user_int = int(input("Type a number"))
user_float = float(input("Type a decimal"))

#the math to add subtract etc
addition = user_int + user_float
subtraction = user_int - user_float
multiplication = user_int * user_float
division = user_int / user_float

#printing out all the results of the math
print("Your numbers added is " + str(addition))
print("Your numbers subtracted is " + str(subtraction))
print("Your numbers multiplied is " + str(multiplication))
print("Your numbers divided is " + str(division))




"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
# creating a dictionary

fruit_dictionary  = {
    "apples" : 5,
    "pears" : 6,
    "grapefruits" : 8
}
#printing one of the values
printing = fruit_dictionary["grapefruits"]
print(str(printing))


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

#string creation

numbers = "1,2,3,4,6,7"

#turns into list
new_list = numbers.split(",")

#turns into tuple
new_tuple = tuple(new_list)

#prints

print(new_tuple)
