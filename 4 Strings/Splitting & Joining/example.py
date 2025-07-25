"""
Quick example showing split and join together.
"""

text = "red green blue"
# Split
colors = text.split()
print(colors)                  # ['red', 'green', 'blue']
# Join
back = "-".join(colors)
print(back)                    # red-green-blue
