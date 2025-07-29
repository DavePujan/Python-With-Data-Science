# parameters_arguments.py

def greet(name, msg="Good Morning"): # name is a required parameter, msg is an optional parameter with a default value
    print(name + ", " + msg)

greet("Poojan") # poojan is argument
greet("Ravi", "Welcome!")
# Output:
# Poojan, Good Morning
# Ravi, Welcome!