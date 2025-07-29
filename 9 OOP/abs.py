# abs - Abstract Class Example
# Definition: Hiding internal details and showing only essential features.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

c = Car()
c.start_engine()

# Use case: Define interfaces without implementation, enforce implementation in child classes.
