"""
Join a list of words back into a single string.
"""

words = ["cat", "dog", "mouse"]
sentence = " ".join(words)      # Join with a space
print(sentence)                 # Output: cat dog mouse

csv = ",".join(words)           # Join with comma
print(csv)                      # Output: cat,dog,mouse
