# WITH.PY - Context Manager Example
# Definition: A context manager is a Python object that defines the runtime context to be established when executing a with statement.

# Definition: Ensures proper resource management using __enter__ and __exit__.
with open("test.txt", "w") as f:
    f.write("Learning OOP with Python")

# No need to call f.close()
