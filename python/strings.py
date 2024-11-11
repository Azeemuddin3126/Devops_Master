# String initialization
s = "Hello, World!"
s2 = 'Python'

# Length of a string
print(len(s))

# Accessing characters (indexing)
print(s[0], s[-1])

# Slicing
print(s[1:5], s[::2])

# Checking if substring exists (in operator)
print('Hello' in s)

# Concatenation
s3 = s + " " + s2
print(s3)

# Repetition
print(s * 2)

# Convert to uppercase/lowercase
print(s.lower(), s.upper())

# Replace substring
print(s.replace("World", "Python"))

# Split string into a list
split_s = s.split(",")
print(split_s)

# Join list into a string
joined_s = "-".join(['a', 'b', 'c'])
print(joined_s)

# Strip whitespaces
s_with_spaces = "  Hello  "
print(s_with_spaces.strip())

# Checking string type
print(s.isalpha(), s.isdigit(), s.isspace())

# String comparison
print(s == "Hello, World!", s < "Hello, Python!")

# String formatting
name = "John"
age = 30
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)

# Count occurrences of a substring
print(s.count("l"))

# Find the index of a substring (raises ValueError if not found)
print(s.find("World"))

# Check if string starts/ends with a certain substring
print(s.startswith("Hello"), s.endswith("!"))

# Case-insensitive comparison
print(s.lower() == "hello, world!".lower())

# String to list of characters
char_list = list(s)
print(char_list)

# String to integer (if possible)
num_str = "123"
num = int(num_str)
print(num)

# Check if string is alphanumeric or numeric
print(s2.isalnum(), num_str.isdigit())

# Check if a string is empty
print(s == "", s2 == "")

# Iterate through each character in a string
s = "Hello, World!"
for char in s:
    print(char)

# Iterate through string and index together
for i, char in enumerate(s):
    print(i, char)

# Iterate over string with condition (only vowels)
vowels = 'aeiou'
for char in s:
    if char.lower() in vowels:
        print(char)

# Create a list of characters using a list comprehension
char_list = [char for char in s]
print(char_list)

# Create a list of uppercase characters from the string
upper_chars = [char for char in s if char.isupper()]
print(upper_chars)

# Create a new string with only non-space characters (using join)
non_space_str = ''.join([char for char in s if char != ' '])
print(non_space_str)

# Iterate over the string and check for a substring (e.g., find "l")
indices = [i for i, char in enumerate(s) if char == 'l']
print(indices)

# Iterate with condition to create a string without vowels
no_vowels = ''.join([char for char in s if char.lower() not in vowels])
print(no_vowels)

# Iterate over string and apply transformations (upper case if vowel)
transformed = [char.upper() if char in vowels else char for char in s]
print(''.join(transformed))

# Reverse a string using slicing and iteration
reversed_s = s[::-1]
print(reversed_s)

# Iterate through string and count occurrences of a character (e.g., 'l')
count_l = sum(1 for char in s if char == 'l')
print(count_l)

print("This program will check to see if two values are the same.")
string1 = input("Enter a value: ").lower()
string2 = input("Enter another value: ").lower()
if string1 == string2:
    print("They are the same!")
else:
    print("They are not the same.")
    
# Define the string
my_string = "Hello"

# Replace vowels with '*'
result = ''.join(['*' if char.lower() in 'aeiou' else char for char in my_string])

# Print the result
print(result)

# Get user input without a prompt
user_input = input()

# Print the first and last characters with context
print(f"{user_input[0]} is the first character and {user_input[-1]} is the last character")

user_input = input()
print((user_input * len(user_input) + '\n') * len(user_input))

txt = input()
for i in range(len(txt)):
    print(txt * len(txt))
    
print(''.join(['u' if c.isupper() else 'l' if c.islower() else '-' for c in input()]))

s = input()
print(s[:len(s) // 2])  # First half
print(s[len(s) // 2:])  # Second half

s = input()
swapped = ''.join(s[i+1] + s[i] for i in range(0, len(s), 2))
print(swapped)

