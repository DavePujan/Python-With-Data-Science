# clssewithp.py - Class with Parameters Example'
# Definition: Initializing class with user-defined data via constructor.
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

s1 = Student("Poojan", 24)
s1.show()
