try:
    print("Inside try")
    x = 1 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
finally:
    print("This will always execute")
# Output:
# Inside try
# Caught ZeroDivisionError
# This will always execute