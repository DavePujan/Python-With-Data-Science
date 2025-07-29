# raise : this is used to trigger an exception manually.
# Custom exceptions can be created by inheriting from the Exception class.
age = -1
if age < 0:
    raise ValueError("Age cannot be negative")
# Output:
# ValueError: Age cannot be negative

# example:
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Your age is:", age)
except ValueError as e:
    print("Error:", e)
# Output:
# Enter your age: -5 
# Error: Age cannot be negative