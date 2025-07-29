try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Ignore the exception silently
print("Program continues...")
# Output:
# Program continues...

# The pass statement allows the program to continue running without any action taken on the exception.
