"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
#imports the datetime function from the datetime module
from datetime import datetime

my_date_time = datetime.now()
# uses this to print the current date and time
print(my_date_time)


"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
#imports date from the datetime module
from datetime import date

#gets todays date without the time
my_date = date.today()
#aranges the date to the right format
my_string = my_date.strftime("%m/%d/%y")
print(my_string)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""
#string 1 and string 2
string1 = "2000/12/2"
string2 = "2003-04-23"

#converts the string to dates
new_date = datetime.strptime(string1, "%Y/%d/%m")
other_date = datetime.strptime(string2, "%Y-%m-%d")

#subtracts the twodates from eachother
delta = other_date - new_date

print(delta.days)


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

#asks user for their birthdate
user_birth = input("When were you born? (dd/mm/yyyy) ")
#converts into a date
user_date = datetime.strptime(user_birth, "%d/%m/%Y")


#todays date 
today_date = date.today()
#finds the time between
delta = today_date - user_date

from_birth = delta.days

print(f"It has been {from_birth} days since birthday")
