# main.py (Program)
import math_functions
import os  # Module for interacting with the operating system

# Get the current working directory
cwd = os.getcwd()
print(cwd)

from library_systems import books

result = math_functions.add(5, 3)
subtract = math_functions.subtract(7,2)
print(f"{subtract} is your answer")
print(result) 

books.add_book("Python Programming", "Fulgencius")