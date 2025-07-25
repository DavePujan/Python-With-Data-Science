"""
Split a string into a list, using spaces or other characters.
"""

text = "apple banana cherry"
words = text.split()          # Default splits at spaces
print(words)                  # Output: ['apple', 'banana', 'cherry']

sentence = "one,two,three"
parts = sentence.split(",")   # Split by comma
print(parts)                  # Output: ['one', 'two', 'three']
