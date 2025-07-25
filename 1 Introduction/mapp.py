# mapp.py - Understanding map() function

# map() applies a function to all items in a list (or any iterable)

def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))

print("Original:", numbers)
print("Squared:", squared)
