# none.py - Understanding None in Python

def greet():
    print("Hello!")
    # No return means it returns None by default

result = greet()
print("Returned:", result)  # Output: None

value = None
if value is None:
    print("value is None")
