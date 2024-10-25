"""
This is python practices a,a
"""
#imports the randint function from the random module
from random import randint

def higher_or_lower(num, val):
    if num > val:
        print("Your number is higher then the corect number")
    if num < val:
        print("Your number is lower than the correct number")

answer = randint(0, 100)
print("A number has been selected. Try to guess it!!")
count = 0

while count < 4 :
    print(f"You have {4-count} attempts left")
    guess = int(input("What is your guess "))
    
    if guess == answer:
        print("You've guessed the number!!! Congraulations!!")
        break
    else:
        higher_or_lower(guess, answer)
        count += 1

if count == 4:
    print(f"You have run out of guesses. The number was {answer}")

    """
This is python practices a,
"""

grocery_list = []

print("Hi, welcome to your grocery list")
print("For some reason this grocery list csn only hold up to five items")