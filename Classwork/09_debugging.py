
#2
text = "Hello, world, my name is"
#defines the count tha is manipulated in the for loop 
count = 0

#loop for each character in the text
for char in text:
    # checks to see it there is a space
    #changed from if char == ""
    if char == " ":
       count += 1

print(count)

#3
print("give me a number")
#takes users num
n = input()

#goes from 1 to n-1
for num in range(1, n):
    #checks if even
    #changed from if num % 2 < 0
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

#4
#takes user integer
num = int(input("Enter an integer: "))

#excludes negative nums
#changes from num < -1
if num < 0:
  print("No negative numbers.")
else:
  result = 1
  #changed from range(1, num):
  for i in range(2, num+1):
    result *= i   

#changed from print("Factorial of " + num + "is" + result)
  print(f"Factorial of {num} is {result}")

#5
#begins at 0 
attempts = 0
#pass= secret
correct_password = "secret"

while True:
    #users password
    password = input("Enter your password: ")
    #adds attempts after guess
    attempts += 1
    
    #checks to see if what the user enteted is correct
    #changes from password == "incorrect_password"
    if password == correct_password:
        print("Correct password!")
        #stopps the loop if the password is correct
        break
    else:
        print("Incorrect password")
    #gives the user 3 attepmts
    #changed from attempts > 3
    if attempts >= 3:
        print("Too many attempts")
        break