# ------------- Tuple Creation -------------
# Basic tuple creation
t = (1, 2, 3)

# Tuple without parentheses
t = 1, 2, 3

# Single-element tuple (note the comma)
single_element_tuple = (1,)

# Tuple from other iterable (e.g., list)
t = tuple([1, 2, 3])

# ------------- Accessing Elements -------------
# Access by index
first = t[0]
last = t[-1]

# Slicing
middle = t[1:3]

# Unpacking tuples
x, y, z = t

# Extended unpacking
a, *rest = t   # `rest` will be a list of the remaining elements
*initial, b = t  # `initial` gets all elements except the last

# Nested tuple unpacking
nested_tuple = (1, (2, 3), 4)
a, (b, c), d = nested_tuple

# ------------- Tuple Immutability -------------
# Tuples cannot be modified in-place, so you must create a new one if you want to change it:
t = (1, 2, 3)
t = t + (4,)  # New tuple with an additional element

# ------------- Concatenation and Repetition -------------
# Concatenate two tuples
t1 = (1, 2)
t2 = (3, 4)
concatenated = t1 + t2

# Repeat a tuple
repeated = t1 * 3

# ------------- Checking Elements -------------
# Check if an element is in the tuple
exists = 2 in t

# Tuple length
length = len(t)

# Count occurrences of an element
count_of_two = t.count(2)

# Find the index of an element (raises ValueError if not found)
index_of_two = t.index(2)

# ------------- Iterating Over Tuples -------------
# Simple iteration
for item in t:
    print(item)

# Iterate with index
for i, item in enumerate(t):
    print(f"Index {i}: {item}")

# ------------- Sorting a Tuple -------------
# Sort elements (returns a sorted list, not a tuple)
sorted_t = sorted(t)

# ------------- Tuple Comprehension Alternative (Generator Expression) -------------
# No direct tuple comprehension (it would create a generator instead)
gen = (x**2 for x in range(5))  # Create a generator

# Convert generator to tuple if needed
squared_tuple = tuple(gen)

# ------------- Converting Between Lists and Tuples -------------
# Convert tuple to list (allows modifications)
t_list = list(t)
t_list.append(4)
t = tuple(t_list)

# Convert list back to tuple
t = tuple(t_list)

# ------------- Summary of Common Tuple Operations -------------
# Basic tuple creation: `(1, 2, 3)` or `tuple([1, 2, 3])`
# Access by index: `t[0]`, slicing: `t[1:3]`
# Unpacking: `a, b, c = t`
# Concatenation: `t1 + t2`
# Repetition: `t * 3`
# Check existence: `2 in t`
# Length: `len(t)`
# Count occurrences: `t.count(2)`
# Find index: `t.index(2)`

# Example showing various tuple operations:
t = (5, 10, 15)
print("First element:", t[0])
print("Tuple length:", len(t))
if 10 in t:
    print("10 is in the tuple.")
for i, val in enumerate(t):
    print(f"Index {i} has value {val}.")
