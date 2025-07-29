# constructor.py - Constructor Example
# Definition: A constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class.
# Definition: The __init__ method is automatically called when a class object is created.
class Laptop:
    def __init__(self, brand):
        self.brand = brand
        print(f"Laptop of {self.brand} brand created.")

l = Laptop("Dell")
