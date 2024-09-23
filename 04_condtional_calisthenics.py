'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
#creates an integr
integer = 23
#checks if integer is even and greater than 10 and returns true or false
print((integer % 2 == 0) and (integer > 10) )


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
#ticket initally has no price
ticket_price = 0
#gets user age
age = int(input("HOw old are you"))
#if less that 18 ticketprice is changed to 10
if age < 18:
    ticket_price = 10
 #if else  ticketprice is changed to 20
else:
    ticket_price = 20
#prints the price of the ticket
print(f"Your price is ${ticket_price} ")


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
#creats a fruit list
fruit_list =["grapes","lychee","apples","pears","jackfruit"]
# askes for users fruit
user_fruit = input("Name a fruit")

#if the users fruit is in the list 
if user_fruit in fruit_list:
    #yes it is
    print("Yes, that fruit is in the list.")
else:
    #no its not
    print("No, that fruit is not in the list.")




'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
#takes users year
user_year = input("Enter a year")

#leap year is divisible by four and century year id divisible by 100
if (user_year % 400 == 0) and (user_year % 100 == 0):
    print("Your year is a leap year AND a century year")
else:
    print("Your year is not a leap year AND century year")

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is LESS THAN 0 kg, return an error message.
so it can be 0????
'''
# Takes the weight and zone from user
weight = float(input("Weight (kg) "))
zone = input("Zone ").lower
cost =  0.0

#makes sure weight is not less that 0
if weight < 0:
    print("Error")
    #checks for zone number
elif zone == "a" or zone == "zone a" or zone == "zonea":
    #calculates price 
    cost = str(weight * 5)
    print ("Your price is " + cost)
    #checks for zone number
elif zone == "b" or zone == "zone b" or zone == "zoneb":
    #calculates price 
    cost = str(weight * 7)
    print ("Your price is " + cost)
    #a little extra
else: 
    print("You need an approiate zone number")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
#asks fpr the three sides of the triangle
side1 = float(input("length of triangle side 1"))
side2 = float(input("length of triangle side 2"))
side3 = float(input("length of triangle side 3"))

# equilateral
if side1 == side2 and side2 == side3:
    print("Your triangle is equilateral triangle")
    #isosceles
#THIS WILL BE DONE