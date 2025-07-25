"""
Check if a string has a certain method.
"""

text = "hello"
print(hasattr(text, "upper"))    # True
print(hasattr(text, "replace"))  # True
print(hasattr(text, "unknown"))  # False
print(text.startswith("he"))  # True
print(text.endswith("lo"))    # True
print(text.isalpha())         # True
print(text.isdigit())         # False
print(text.isalnum())         # True