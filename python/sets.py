# ------------- Set Creation -------------
# Basic set creation (unordered and unique elements)
s = {1, 2, 3, 4}

# Creating an empty set (use set() as {} creates an empty dictionary)
s = set()

# Creating a set from a list (removes duplicates)
s = set([1, 2, 3, 4, 4, 5])

# ------------- Adding and Removing Elements -------------
# Add a single element
s.add(6)       # s becomes {1, 2, 3, 4, 5, 6}

# Add multiple elements with update (any iterable can be used)
s.update([7, 8, 9])  # s becomes {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Remove an element (raises KeyError if the element does not exist)
s.remove(4)

# Discard an element (does not raise an error if the element is missing)
s.discard(10)

# Remove and return an arbitrary element
removed_element = s.pop()

# Clear all elements from the set
s.clear()

# ------------- Set Operations -------------
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Union (elements in either set)
union_set = s1 | s2   # or s1.union(s2)

# Intersection (elements in both sets)
intersection_set = s1 & s2  # or s1.intersection(s2)

# Difference (elements in s1 but not in s2)
difference_set = s1 - s2  # or s1.difference(s2)

# Symmetric Difference (elements in either set, but not both)
symmetric_difference_set = s1 ^ s2  # or s1.symmetric_difference(s2)

# ------------- Checking Subset and Superset Relationships -------------
# Check if s1 is a subset of s2
is_subset = s1 <= s2  # or s1.issubset(s2)

# Check if s1 is a proper subset of s2 (s1 <= s2 and s1 != s2)
is_proper_subset = s1 < s2

# Check if s1 is a superset of s2
is_superset = s1 >= s2  # or s1.issuperset(s2)

# ------------- Set Membership -------------
# Check if an element is in a set
exists = 3 in s1

# Check if an element is not in a set
not_exists = 6 not in s1

# ------------- Iterating Over Sets -------------
# Simple iteration
for item in s1:
    print(item)

# ------------- Set Comprehension -------------
# Create a set of squares
squares = {x**2 for x in range(10)}

# ------------- Common Set Methods -------------
# Add element: `s.add(10)`
# Update with multiple elements: `s.update([11, 12])`
# Remove element (raises KeyError if missing): `s.remove(3)`
# Discard element (no error if missing): `s.discard(3)`
# Pop element: `s.pop()`
# Clear set: `s.clear()`
# Check subset: `s1 <= s2`
# Check superset: `s1 >= s2`

# Example showing various set operations:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

if 3 in s1:
    print("3 is in s1.")

# Iterating over the set
for element in s1:
    print("Set element:", element)