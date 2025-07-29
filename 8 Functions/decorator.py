# decorator.py - Function decorator example

# definition of a decorator: A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
def decorator_func(original_func): 
    def wrapper():
        print("Before function call")
        original_func()
        print("After function call")
    return wrapper

@decorator_func # Applying the decorator
def say_hello():
    print("Hello!")

say_hello() 
# Output: 
# Before function call
# Hello! 
# After function call
