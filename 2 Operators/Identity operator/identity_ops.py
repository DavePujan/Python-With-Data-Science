# identity_ops.py - Identity Operators

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)     # False (different objects)
print("x is z:", x is z)     # True (same object)
print("x is not y:", x is not y)
