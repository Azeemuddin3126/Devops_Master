#-----------------------------------
 #parameters
#--------------------------------

def add_sub(num1, num2, num3):
    """add_sub does the following:
    Add the first two parameters
    Subtract the third paramter
    Print the result"""
    print(num1 + num2 - num3)

add_sub(5, 10, 15)

 #Named Parameters
#--------------------------------

def subtract(num1, num2):
  """Substract the 2nd paramater the 1st"""
  print("The subtract of 2 numnbers is : ",num1 - num2)
subtract(5,2)
subtract(2,5)
subtract(num2=3, num1=5)


 #Checking Parameters
#--------------------------------

def addition(num1, num2):
    """Add the two parameters together
    Use try/except to catch any errors"""
    try:
        print(num1 + num2)
    except:
        print("There is an error in your code.")
    
addition(5, "cat")


 #Optional Parameters
#--------------------------------
def add_if_true(num1,num2,bool=True):
  if bool:
    print(num1+num2)
  else:
    print("No addition, bool is false")
add_if_true(5,7)
add_if_true(5,7, False)

def cal_sum(*nums):
  total=0
  for i in nums:
    total+=i
  print(total)

cal_sum(1,2,3,5,6)
#-------------------
# Shorthand function to calculate the sum of numbers
def cal_sum(*nums):
    print(sum(nums))

# Taking user input and converting it to integers
user_input = map(int, input("Enter numbers separated by spaces: ").split())

# Passing unpacked user input to the function
cal_sum(*user_input)


#-----------------------------------
 #Varible Scope
#--------------------------------
greet="welcome" #global
def say():
  print(greet) #local
say()
print(greet)
#------------------
def say_hello():
    """Demonstrate how to use the global keyword"""
    global greeting
    greeting="Hello"
    greeting = "Bonjour"
    print(greeting)

say_hello()
print(greeting)


#-----------------------------------
 # Returing Values
#--------------------------------

def add_five(num):
    """Add five to the parameter num"""
    return(num + 5)
  
new_number = add_five(10)
print(new_number)


#-------------------------------

def avg(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (a + b) / 2
    else:
        return "Please use two numbers as parameters"

# Example calls to test the function
print(avg(10, 25))  # Expected output: 17.5
print(avg(10, "cat"))  # Expected output: Please use two numbers as parameters


def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")
#---------------------------------

def odds_or_evens(is_even, numbers):
    return [num for num in numbers if (num % 2 == 0) == is_even]

# Test cases
print(odds_or_evens(True, [13, 22, 8, 31]))    # Output: [22, 8]
print(odds_or_evens(False, [13, 22, 8, 31]))   # Output: [13, 31]

#---------------------------------------------

def search_list(items, term):
    term_lower = term.lower()
    for i, item in enumerate(items):
        if item.lower() == term_lower:
            return i
    return -1

# Test cases
print(search_list(["dog", "fish", "cat"], "Cat"))    # Output: 2
print(search_list(["water", "Toy", "house"], "toy")) # Output: 1
print(search_list(["box", "car", "hat"], "mouse"))   # Output: -1

def search_list(items, term):
    return next((i for i, item in enumerate(items) if item.lower() == term.lower()), -1)

# Test cases
print(search_list(["dog", "fish", "cat"], "Cat"))    # Output: 2
print(search_list(["water", "Toy", "house"], "toy")) # Output: 1
print(search_list(["box", "car", "hat"], "mouse"))   # Output: -1

def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for i, item in enumerate(lst):
        if item.lower() == term.lower():
            return i
    return -1

#------------------------------------

import csv

def best_team(mlb_data):
    with open(mlb_data, "r") as file:
        reader = csv.DictReader(file)
        return max(reader, key=lambda row: int(row["W"]))["Tm"]
#-----------------------------

def is_palindrome(s):
    return s == s[::-1]
    


