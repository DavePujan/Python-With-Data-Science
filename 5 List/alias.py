# alias.py - Aliasing and references

a = [1, 2, 3]
b = a  # both refer to same object
b[0] = 100
print("a:", a)  # [100, 2, 3]
