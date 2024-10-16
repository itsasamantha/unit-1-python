"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b

# checks for 9/3 = 3
assert divide(9,3) == 3
# checks for 0/5  = 0
assert divide(0,5) == 0
# checks for 57/0  = Nothing
assert divide(57,0) == None

#EXTRA CREDIT
#checks if divide 7/8 is 3 
#if it causees an assertion error it will then pass and not alert in console
try:
  assert divide(7,8) == 3
except:
  pass






"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  


# checks for the factorial of 3  = 6
assert factorial(3) == 6
# checks for the factorial of 3  = 6
assert factorial(0) == 1

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

# makes sure strings becomes sgnirts
assert reverse_string("strings") == "sgnirts"

#makes sure yoland becons dnaloy
assert reverse_string("yoland") == "dnaloy"


"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
  
# makes sure the 6th term in the fibonacci sequenceis 8
assert fibonacci(6) == 8
#makes sure that the 15th term in the fibonacci sequence is 610
assert fibonacci(15) == 610


"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None


#makes sure that the emaiil newacraZy@HYbeGeffn.org is a valid email
assert is_valid_email("newacraZy@HYbeGeffn.org") == True

#makes sure that KATSEYE@carzy,wp is not a valid email
assert is_valid_email("KATSEYE@carzy,wp") == False