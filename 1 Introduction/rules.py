# rules.py - Python Naming Rules and Conventions

# Variable names must begin with a letter or underscore
name = "Poojan"
_age = 20  # Valid
# 2cool = 50  # Invalid, can't start with a number

# Avoid using Python keywords like `for`, `if`, etc.

# Naming convention: snake_case for variables and functions
def calculate_area(length, width):
    return length * width
