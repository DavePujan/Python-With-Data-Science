"""
Count how many vowels (a, e, i, o, u) are in a string.
"""

text = "Programming"
count = 0
for letter in text:
    if letter in "aeiouAEIOU":
        count += 1
print(count)  # Output: 3
