import math
print("Welcome to the Calculatinator-inator 9000!")
# asking the user for two varibles
resutl = 0

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# printing out all the options spaced out
print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")

#asking the user for their choice
choice = int(input("Enter choice: "))
# going through the choices
# only did it like this so i can add the else statement
if choice == 1:
    result = num1 + num2
elif choice == 2:
    result = num1 - num2
elif choice == 3:
    result = num1 * num2
elif choice == 4:
    result = num1 / num2
elif choice == 5:
    #math.floor(num1 / num2)
    result = num1 // num2
elif choice == 6:
    #pow(num1,num2)
    result = num1 ** num2
elif choice == 7:
    #math.remainder(num1 / num2) 
    result = num1 % num2
else:
    result = "You need to choose one of those options"

print(result)

    