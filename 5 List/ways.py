# ways.py - Different ways to create a list

a = list()  # empty


b = [1, 2, 3] # list with elements

# Using range() to create a list of numbers
c = list(range(5))
print(a, b, c)

# Using list comprehension
d = [x for x in range(5)]
print("List comprehension:", d)

# Using the list() constructor with a string
e = list("hello")
print("List from string:", e)

# Using the list() constructor with a tuple
f = list((1, 2, 3))
print("List from tuple:", f)

# Using the list() constructor with a set
g = list({1, 2, 3})
print("List from set:", g)

# Using the list() constructor with a dictionary
h = list({"a": 1, "b": 2})  
print("List from dictionary keys:", h)

