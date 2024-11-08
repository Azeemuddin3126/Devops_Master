#----------------------------------
# Printing
#-----------------------------------
print("hello world")
print("hello", end='/n')  # "", "\t", "\!"
print("world")

#----------------------------------
# Comments
#-----------------------------------
# comments
'''
multi-line comment
'''

#----------------------------------
# Data Types
#-----------------------------------
my_variable = "Hello world"
print(my_variable)
my_variable = "Goodbye world"
print(my_variable)

string_variable = "This is a string"
second_string = 'This is a string also'
print(string_variable, second_string)

boolean_variable = True
print(boolean_variable)

integer_variable = 50  # 5,000 #050
float_variable = 50.0, 50., .001
print(integer_variable, float_variable)

#----------------------------------
# Arithmetic Operations
#-----------------------------------
a, b = 20.0, 10
print(a + b, a - b, a / b, a // b, a * b, 3 * "hello", a ** b, a % b)

# Increment
a, b = 0, 0
a += 1
b -= 1
print(a, b)

# Type Casting
a = 3
print(type(a))
a = str(a)
print(type(a))

b = "3"
print(a + int(b))

# String Concatenation
a, b = "This is an ", "example string"
print(a + b)

# Order of Operations
result = 3 * a ** 3 / (b + 5) + c
print(result)  # PEMDAS

#----------------------------------
# Boolean Operations
#-----------------------------------
a = b = True
c = False
print(a and c and a and b and a)
print(a or c)
print(not (True and False))
print(not True and False)
print(not not True)
print(3 < 4 and 1 > 0)
print(10 > 6 or 6 < 5)
print(10 > 12 or 20 > 4)
print(not b and not a or not not c)

# Example Simplified
print(True and not a or not not c)  # False

#----------------------------------
# Conditional Statements
#-----------------------------------
if 7 != 10:
    print("The above statement is true")
print("This is not related to the if statement")

# Grade
grade = 90
if grade > 70:
    print("Congrats, you passed the class")
else:
    print("Condolences, you did not pass the class")

# Number check
num = 4
print(f"{num} is an {'even' if num % 2 == 0 else 'odd'} number")

# Compound Conditions
num = 16
if num % 2 == 0 and num > 10:
    print("Even and greater than 10")

# If-elif-else
grade = 82
if grade < 70:
    print("You got an F.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

#----------------------------------
# Loops
#-----------------------------------
for i in range(5):
    print(f"Loop #{i}")

for i in range(10, 0, -1):
    print(i)

for i in range(0, 10, 2):
    print(i)

# Sum 0 to 100
total = sum(range(101))
print(total)

# While loop example
count = 0
while count < 5:
    print("hello")
    count += 1

# Infinite loop with break
import random
while True:
    print("This is an infinite loop")
    rand_num = random.randint(1, 101)
    if rand_num > 75:
        print("The loop has ended")
        break

# Nested Loop
for row in range(10):
    print("#" * 10)

# More complex nested loops
for i in range(5):
    for j in range(10):
        print('#' if i % 2 == 0 else '*', end='')
    print()

# Multiplying Exponentiation example
exp, base = 4, 2
result = base ** exp
print(result)

# Nested pattern
for row in range(8):
    for column in range(8):
        print('X' if (row + column) % 2 == 0 else 'O', end='')
    print()

#----------------------------------
# While Loop Sum
#-----------------------------------
total, count = 0, 0
while count <= 100:
    total += count
    count += 1
print(total)
