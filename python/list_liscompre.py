# Task 1: List comprehension that returns the square of each number from 0 to 15
squares = [x**2 for x in range(16)]
print(squares)

# Task 2: List comprehension that returns numbers from 0 to 20 with 4 as a factor
['true' if x % 4 == 0 else 'false' for x in range(21)]
factors_of_4 = [x for x in range(21) if x % 4 == 0]
print(factors_of_4)

# Task 3: Generator function that returns 'foo' every fifth call and 'moo' otherwise
def foo_moo():
    i = 1
    while True:
        if i % 5 == 0:
            yield 'foo'
        else:
            yield 'moo'
        i += 1

# Create an instance of the generator
fm = foo_moo()

# Test the generator by calling next() 11 times
for _ in range(11):
    print(next(fm))

# Task 4: Dictionary comprehension using 'name' to create a dictionary
name = 'hemri'  # Replace 'hemri' with your actual name
items = zip(list(name), list(range(len(name))))
name_dict = {x: y for x, y in items}
print(name_dict)
