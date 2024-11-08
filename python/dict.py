# ------------- Dictionary Creation -------------
# Basic creation
d = {"name": "Alice", "age": 25}

# Create from lists of keys and values
keys = ["name", "age", "location"]
values = ["Alice", 25, "NYC"]
d = dict(zip(keys, values))

# From keys with a default value
d = dict.fromkeys(["key1", "key2"], "default")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}

# ------------- Accessing Values -------------
# Access a value safely with .get (avoids KeyError)
name = d.get("name", "default_value")

# Direct access (raises KeyError if key doesn’t exist)
age = d["age"]

# Check if a key exists
exists = "name" in d

# Get all keys, values, or items
keys = list(d.keys())
values = list(d.values())
items = list(d.items())

# ------------- Adding and Updating -------------
# Add or update a key-value pair
d["location"] = "California"

# Update multiple items with another dictionary
d.update({"name": "Bob", "age": 30})

# Python 3.9+ merging dictionaries with |
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2

# ------------- Removing Elements -------------
# Remove a specific key (add default to avoid KeyError if key is missing)
d.pop("age", "default_if_not_found")

# Remove and return the last item (Python 3.7+)
last_key, last_value = d.popitem()

# Clear the dictionary
d.clear()

# ------------- Information About Dictionary -------------
# Dictionary length
length = len(d)

# Check if dictionary is empty
is_empty = not d

# Copy dictionary
d_copy = d.copy()

# Sort by keys or values (sorted returns list)
sorted_keys = sorted(d.keys())
sorted_items_by_values = sorted(d.items(), key=lambda item: item[1])

# ------------- Iteration with Dictionaries -------------
# Iterate through keys
for key in d:
    print(key)

# Iterate through values
for value in d.values():
    print(value)

# Iterate through key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

# ------------- Dictionary Comprehensions -------------
# Filter and modify during creation
filtered_dict = {k: v for k, v in d.items() if isinstance(v, int)}

# Reverse keys and values
reversed_dict = {v: k for k, v in d.items()}

# ------------- Counting and Aggregating -------------
# Count occurrences of values
counts = {k: d.get(k, 0) + 1 for k in d}

# Sum, min, max of dictionary values (for numeric values only)
total = sum(d.values())
min_val = min(d.values())
max_val = max(d.values())

# ------------- Common Methods Summary -------------
# `.clear()` - Removes all items from dictionary
# `.copy()` - Returns a shallow copy of dictionary
# `.get(key, default)` - Returns value for `key`, or `default` if `key` is not found
# `.items()` - Returns a view of (key, value) pairs
# `.keys()` - Returns a view of keys
# `.pop(key, default)` - Removes specified key and returns the value, or `default` if key not found
# `.popitem()` - Removes and returns an arbitrary (key, value) pair
# `.setdefault(key, default)` - Returns value of `key`, sets it to `default` if `key` not found
# `.update(other)` - Updates dictionary with key-value pairs from `other` dictionary or iterable
# `.values()` - Returns a view of values

# ------------- Summary Examples -------------
# Example of accessing, modifying, deleting, and iterating over dictionaries:
d = {"name": "Charlie", "age": 28, "city": "LA"}
print(d["name"])            # Access value by key
d["city"] = "New York"      # Modify value
d.update({"age": 29})       # Update value
d.pop("city")               # Remove key
for k, v in d.items():      # Iterate over items
    print(k, v)
