# set_example.py - Working with Sets

# A set is a collection which is unordered and unindexed
numbers = {1, 2, 3, 4, 4, 5}
print("Set:", numbers)  # Duplicates are automatically removed

# Adding
numbers.add(6)

# Removing
numbers.discard(2)

# Set operations
odds = {1, 3, 5}
evens = {2, 4, 6}

# Union
print("Union:", odds | evens)

# Intersection
print("Intersection:", odds & evens)

# Difference
print("Difference:", odds - evens)
