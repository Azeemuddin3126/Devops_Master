#------------------------------------------------------------------------------------------------
# Step 1: Create a dictionary with your name and age
person = dict(Name="YourName", Age=18)  # Replace "YourName" with your actual name and "18" with your age
print(person)

# Step 2: Add your name and age to a list of lists, then use it to create a dictionary
data = [['Name', 'YourName'], ['Age', 18]]  # Replace "YourName" and "18" with your actual values
person_from_data = dict(data)
print(person_from_data)

# Step 3: Add your name and age to the following dictionary
person_updated = {'Name': 'YourName', 'Age': 18}  # Replace "YourName" and "18" with your actual values
print(person_updated)

#------------------------------------------------------------------------------------------------------

# Step 1: Create a dictionary named 'codes' with keys 'left' and 'right' and values 'red' and 'green'
codes = {'left': 'red', 'right': 'green'}

# Step 2: Set the variable codes_keys to the keys view from the dictionary
codes_keys = codes.keys()
print(codes_keys)  # Output should be: dict_keys(['left', 'right'])

# Step 3: Set the variable codes_values to the values view from the dictionary
codes_values = codes.values()
print(codes_values)  # Output should be: dict_values(['red', 'green'])

# Step 4: Set the variable codes_items to the items view from the dictionary
codes_items = codes.items()
print(codes_items)  # Output should be: dict_items([('left', 'red'), ('right', 'green')])

# Step 5: Update the value of the key 'left' in codes to 'blue'
codes['left'] = 'blue'

# Step 6: Print the updated values for codes_keys, codes_values, and codes_items
print(codes_keys)   # Output should now show: dict_keys(['left', 'right'])
print(codes_values) # Output should now show: dict_values(['blue', 'green'])
print(codes_items)  # Output should now show: dict_items([('left', 'blue'), ('right', 'green')])

# Step 7: Add a new key-value pair to codes: 'middle': 'yellow'
codes['middle'] = 'yellow'

# Print the values for codes_keys, codes_values, and codes_items again to see the updates
print(codes_keys)   # Output should now show: dict_keys(['left', 'right', 'middle'])
print(codes_values) # Output should now show: dict_values(['blue', 'green', 'yellow'])
print(codes_items)  # Output should now show: dict_items([('left', 'blue'), ('right', 'green'), ('middle', 'yellow')])

#-------------------------------------------------------------------------------------------------------------------