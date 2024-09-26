"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#for loop that iterates from 1 to 10
for x in range (1,11):
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
# sets the range to 900 to 1000 and makes sure it counts by ten
for x in range(900,1001,10):
    print(x)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
# makes counts through 1-100 by 9s
for x in range(1,101,9):
    print(x)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#sets the sum value
sum = 0
# counts throught 1-10 and adds all the numbers together
for x in range(1,11):
    sum +=x

print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?


- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# The output of this code is:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# This code sets rows to 5 and counts through each row
# on the first iteration the second for loop runs 
#currently i is equal to 0 so 0+1 is 1  and range() runs once
#so it prints * and a space
#(guessing end puts the space at the end but does not end the line or allows a nother print statement like it to continue)
# since the range is done it runs the empthy print statement and starts again from the first for loop increasing i to 1
# again it runs the second loop i=1 now is 2 so it runs twice
# doing the same thing but now it print * space * space
# this stops after i=4 or the fifth iteration