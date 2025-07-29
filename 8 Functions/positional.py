# positional.py - Positional arguments

def student(name, age):
    print(name, "is", age, "years old")

student("Poojan", 19)
# Output: Poojan is 19 years old

# Wrong
def student1(name,age):
    print(name, "is", age, "years old")

student1(19, "Poojan")  # This will not work as expected
# Output: 19 is Poojan years old