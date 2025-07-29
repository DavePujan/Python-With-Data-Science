# inheritance.py - Inheritance Example
# Definition: A mechanism where a new class inherits attributes and methods from an existing class.

# Use case: Allows code reuse and establishes a relationship between classes.

# Definition: One class (child) inherits features from another (parent).

class Parent:
    def show(self):
        print("This is parent class.")

class Child(Parent):
    def display(self):
        print("This is child class.")

c = Child()
c.show()
c.display()
