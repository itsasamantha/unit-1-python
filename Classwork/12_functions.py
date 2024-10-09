"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""
#inputed name 
user_name  = input("What is your name? ")

def greeting (name):
    print("Hello, " + name)

greeting(user_name)
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#takes an integer from user 
#turns to int
user_int  = int(input("What is your integer? "))

#function that squares the paramenter int
def square (int):
    return int ** 2

#the returned numberis saved to this varible
squared_num = square(user_int)


"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
#takes the users number
user_number = int(input("Write a number "))

# returns the string 'true' or 'false'
def t_or_f(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"

even_or_odd = t_or_f(user_number)


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
#function the uses two paramaters
def area(length, width):
    return length * width

calculations = area(3,7)


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

#sets the celcius value
celsius_temp = 43.6

#preforms the conversion equation and returns it 
def convert(cel):
    return (cel*(9/5))+32
#sets the returned value to fahrenheit_temp
fahrenheit_temp = convert(celsius_temp)


"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
#list of numbers
num_list = [23,3,23,1,14,5,6,7,24,12,23]

def average(list):
    sum = 0
    count = 0
    
    for x in list:
        #adds each num in list
        sum += x
        #counts each num 
        count += 1 
    return sum/count
#saves the returned num
average_of_list = average(num_list)

"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""