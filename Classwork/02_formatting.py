"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
#creatinga password
password = "ThisismyPassword!"
#asking user for their password
pass_input = input("What is your password")
#converting both to lower case so that case does not matter
password = password.lower()
pass_input = pass_input.lower()

#checks if the password is the same
if pass_input == password:
    print("Correct password")
else:
    print("Incorrect password")



"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

#User input
information = input("Write your name")
#removes excess spaces
information = information.strip()

#checks if string is empty and prints response
if bool(information) == True:
    print("Valid")
else:
    print("Invalid")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

sentence = "I saw a Cat run up to the Cat in the hat."
sentence = sentence.lower()
#replaces every instance of cat
new_sentence = sentence.replace("cat", "dog")
#prints new sentence
print(new_sentence)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

#takes users name and age
user_name = input("What's your name? ")
user_age = int(input("How old are you"))

# formatts 
phrase = f"Your name is {user_name} and you are {user_age} years old"
#prints name and age
print(phrase)


"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
#asks user for two floats
float_one = float(input("Type a decimal"))
float_two = float(input("Type a second decimal"))

#maths the quotient
quotient = float_one/float_two

#rounds
rounded_quotient = round(quotient ,1)

result = f"Result: {rounded_quotient}"
print(result)


#It didnt say it needed to be rounded using {0:.1f}

