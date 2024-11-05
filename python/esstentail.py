import random

# Generate a list of 10 random integers between 1 and 5
numbers = [random.randint(1, 5) for _ in range(10)]
print(numbers)

# Check if the number 4 is in the list and count occurrences
if (count := numbers.count(4)) > 0:
    print(f"{count} fours found")
else:
    print("No fours found")
    
if 4 in numbers:
    count_of_fours = numbers.count(4)
    print(f"Number of fours found: {count_of_fours}")
else:
    print("No fours found")

# Sort and then reverse the list
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# Assign first item to a, middle items to b, last item to c
a, *b, c = numbers
print(a)
print(b)
print(c)

# Convert numbers to a set of unique values
unique_numbers = set(numbers)
print(unique_numbers)

# Create a dictionary with numbers and unique_numbers
number_records = {"numbers": numbers, "unique_numbers": unique_numbers}
print(number_records)
