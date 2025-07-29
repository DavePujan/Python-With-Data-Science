# operators.py - Operator Overloading Example
# Definition: Allowing user-defined classes to implement behavior for built-in operators.

# Definition: Using special methods to redefine the meaning of operators for objects.
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Point(self.x + other.x)

    def __str__(self):
        return str(self.x)

p1 = Point(5)
p2 = Point(3)
print(p1 + p2)
# Output: 8

# Use case: Custom behavior for operators like +, -, *, etc. in user-defined classes.