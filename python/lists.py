# Printing lists
int_list, string_list, mixed_list = [1, 2, 3, 4, 5], ["John", "Paul", "George", "Ringo"], [0.87, "hello", True, 17]
print(int_list, string_list, mixed_list)

# List Comprehension
my_list = [i for i in range(1, 51)]
print(my_list)

# Indexing
my_list = [5, 10, 15, 20]
print(my_list[0], my_list[2], my_list[-1])
my_list[0], my_list[1], my_list[2] = 4, 5, 6
print(my_list)

# List Concatenation
print([1, 2, 3] + [4, 5, 6], [4, 5, 6] + [1, 2, 3])

# List Repetition
print(["Hi!"] * 4)

# IN operator
my_list = ["red", "orange", "yellow", "green"]
print("red" in my_list)

# Length
l1, l2 = [12, 66, 52, 97, 28, 41, 7], [i for i in range(0, 20)]
print(len(l1), len(l2))
print('l1 is longer than l2' if len(l1) > len(l2) else 'l1 and l2 are the same' if len(l1) == len(l2) else 'l2 is longer than l1')

# Slicing
my_list = ["red", "orange", "yellow", "green"]
print(my_list[0:2], my_list[1:2], my_list[::-1])

# Append
my_list = [1, 2, 3]
my_list.append([4, 'four', len(my_list), my_list[0]])
print(my_list)

# POP
my_list = [1, 2, 3, 4]
my_list.pop(), my_list.pop(-1)
print(my_list)

# Insert
my_list = [1, 2, 3, 4]
my_list.insert(2, "Hi")
print(my_list)

# Remove
my_list = [1, 2, 3, 3, 4]
my_list.remove(2), my_list.remove(4)
print(my_list)

# Count
my_list = [2, "red", 2.0, 2, "Red", 8 // 4]
print(my_list.count(2), my_list.count('Red'))

# Index
my_list = ["dog", True, 16, "house", 55.9, False, 16]
print(my_list.index("house"))

# Sorting
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print("Ascending:", sorted(my_list), "Descending:", sorted(my_list, reverse=True))

# Reversing
my_list = ["north", True, 45, 12, "red"]
print("Original:", my_list, "Reversed:", my_list[::-1])

# Average Calculation
my_list = [5, 17, 2, 3, 3]
avg = sum(my_list) / len(my_list)
print(avg)

# Min and Max
my_list = [45, 12, 9, 1, -1, -0.2]
print(min(my_list), max(my_list))

# List Iteration
numbers = [1, 2, 3, 4]
for number in numbers:
    print(number)

# Nested Lists
pets = [['dogs', 'labrador', 'german shepherd', 'golden retriever'], ['cats', 'siamese', 'persian', 'maine coon']]
print(pets, pets[0][1])

numbers = [[11, 13, 22, 76, 54], [2, 65, 107, 112, 8], [33, 90, 34, 7, 804]]
for row in numbers:
    for column in row:
        print('even' if column % 2 == 0 else 'odd')

# Random Nested Lists
import random
numbers = [[random.randint(1, 101) for _ in range(10)] for _ in range(10)]
for row in numbers:
    print(" ".join(map(str, row)))

# Sorting 2D list
numbers = [[6, 7, 10, 9, 8], [12, 13, 14, 11, 15], [20, 18, 17, 19, 16], [1, 2, 3, 4, 5]]
numbers.sort()
for row in numbers:
    row.sort()
    print(row)

# Total of 2D list
total = sum(sum(row) for row in numbers)
print(total)

# Separate Odd and Even Numbers
numbers = [random.randint(0, 100) for _ in range(20)]
odd, even = [num for num in numbers if num % 2 != 0], [num for num in numbers if num % 2 == 0]
print("Odd:", odd, "Even:", even)

# Sum of Numbers
numbers = [random.randint(0, 100) for _ in range(20)]
print(sum(numbers))

# Middle Third of a List
numbers = [random.randint(0, 100) for _ in range(9)]
middle = numbers[len(numbers)//3 : len(numbers)//3 * 2]
print(middle)

# List comprehension to categorize even/odd
result = ['odd' if num % 2 != 0 else 'even' for num in numbers]
print(result)

# Shorthand for string transformation
numbers = ['*' if num > 10 else num for num in numbers]
print(numbers)

# Shorthand for list multiplication or assignment
output = my_list * 3 if len(my_list) < 5 else my_list
print(output)

# Sorting first string in list
first_string = sorted(strings)[0]
print(first_string)

# Increment sequence
numbers += [numbers[-1] + 1, numbers[-1] + 2]
print(numbers)

# Updating a 2D list
for i in range(number):
    data[i][i] = 1
    print(' '.join(map(str, data[i])))
