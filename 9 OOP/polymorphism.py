# polymorphism.py - Polymorphism Example
 
# Definition: One interface, many implementations.
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())
