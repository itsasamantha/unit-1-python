"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#asks user for a string
user_string = input("Write word")
#for loop that takes each character of the string
for x in user_string:
    #and prints it
    print(x)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#list of numbers
num_list = [1,2,3,4,5,6,7,8,9]
#creating the sum var out side of the loop
sum = 0

for x in num_list:
    sum += x

print(sum)

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#asks user for a sentence
sentence = input("Write a sentence")
#turns each word into a list
new_list= list(sentence.split(" "))
 # for each word it tells the length of each word
for x in new_list:
    #gets the length
    print(len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result
"""
#creates dictionary
apple_dictionary = {
  "pome_fruit": True,
  "has_core": True,
  "color": "red",
  "has_seed": True
}
#prints the dictionary
for x in apple_dictionary:
    print(x)


"""
In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

# The code did not print the value with the keys. This is not entirely what I expexted because it thought it would print the pairs