output_file = open("student_folder/text/practice1.txt", "w")
output_file.close()

output_file = open("student_folder/text/practice1.txt", "w")
output_file.writelines("Hello there")
output_file.close()


output_file = open("student_folder/text/practice2.txt", "w")
output_file.writelines("Hello")
output_file.writelines("there")
output_file.close()

lines_to_write = ["First sentence.", "Second sentence.", "Third sentence."]
output_file = open("student_folder/text/practice2.txt", "w")
output_file.writelines(lines_to_write)
output_file.close()

output_file = open("student_folder/text/practice3.txt", "w")
output_file.writelines("First sentence")
output_file.close()

with open("student_folder/text/practice3.txt", "a") as output_file:
    output_file.writelines("Some new text!")

import csv

with open("student_folder/csv/monty_python_movies.csv", "r") as input_file:
    reader = csv.reader(input_file)
    for row in reader:
        print(row)
        
import csv

with open("student_folder/csv/home_runs.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader) #skip the header row
    for row in reader:
        print(row)
        
import os
from pathlib import Path

# 1. Open a file for reading and print its content
with open('example.txt', 'r') as file:
    content = file.read()
    print(f"File Content: \n{content}")

# 2. Read the file line by line using readline()
with open('example.txt', 'r') as file:
    line = file.readline()
    print(f"First line: {line}")

# 3. Read all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f"All lines: {lines}")

# 4. Writing to a file (overwrite content)
with open('output.txt', 'w') as file:
    file.write("Hello, world!\nThis is a new file content.")

# 5. Appending to a file
with open('output.txt', 'a') as file:
    file.write("\nAppended this line.")

# 6. Writing a list of strings to a file
with open('output.txt', 'w') as file:
    file.writelines(["First line.\n", "Second line.\n", "Third line.\n"])

# 7. Using a context manager to automatically close the file
with open('output.txt', 'r') as file:
    print(file.read())  # File is automatically closed after the block

# 8. Checking if a file exists
file_path = 'example.txt'
if os.path.exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")

# 9. Renaming a file
old_name = 'oldfile.txt'
new_name = 'newfile.txt'
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"Renamed {old_name} to {new_name}")

# 10. Deleting a file
if os.path.exists(new_name):
    os.remove(new_name)
    print(f"Deleted {new_name}")

# 11. Get file size using os.stat()
file_size = os.stat('example.txt').st_size
print(f"File size of example.txt: {file_size} bytes")

# 12. Checking file properties using pathlib
file = Path('example.txt')
if file.exists():
    print(f"File name: {file.name}")
    print(f"File extension: {file.suffix}")
    print(f"Is it a file? {file.is_file()}")
    print(f"Is it a directory? {file.is_dir()}")

# 13. File Positioning: seek and tell
with open('example.txt', 'r') as file:
    print("Initial position:", file.tell())  # Tell the current position
    file.seek(5)  # Move the cursor to position 5
    print("Position after seek:", file.tell())  # Tell the new position
    print(file.read(5))  # Read 5 characters from the current position

# 14. Using split() to process text
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()  # Split content by whitespace
    print(f"Words in the file: {words}")


