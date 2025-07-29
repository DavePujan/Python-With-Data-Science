# except_as.py - Example of using 'as' in exception handling

try:
    num = int("abc")
except ValueError as err:
    print("Error:", err)
# Output:
# Error: invalid literal for int() with base 10: 'abc'

# The 'as' keyword allows you to capture the exception object and use it later in your code, which can be useful for logging or debugging.