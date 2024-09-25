"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 0
while i < 10:
    i +=1
    print(i)

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
i=10
while i >= 1:
    print(i)
    i-=1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

num = int(input("Write a number "))
factorial = num
while num > 1:
    num -=1
    factorial = factorial*num

print(factorial)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = "rumpelstiltskin"


while True:
    user = input("Guess my password(case sensitive))")
    if user == password:
        print("You've guessed my password")
        break
    else:
        print("Try again")



"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""