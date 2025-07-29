# encapsu.py - Encapsulation Example

# Definition: Wrapping data and methods into a single unit; restricts access.
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amt):
        self.__balance += amt

    def show(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(5000)
acc.show()
# acc.__balance = 1000  # Won’t work due to name mangling
