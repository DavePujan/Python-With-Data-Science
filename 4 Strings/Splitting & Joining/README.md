# Splitting & Joining

This directory contains functions and examples related to splitting and joining strings in Python.

## Splitting Strings

Splitting a string means breaking it into a list of substrings based on a specified delimiter. The most common method for splitting strings in Python is the `split()` method.

### Example:
```python
text = "Hello, World!"
words = text.split(", ")
print(words)  # Output: ['Hello', 'World!']
```

## Joining Strings

Joining strings involves combining a list of strings into a single string with a specified separator. The `join()` method is used for this purpose.

### Example:
```python
words = ['Hello', 'World!']
text = ", ".join(words)
print(text)  # Output: 'Hello, World!'
```

## Usage Instructions

1. Use the `split()` method to divide a string into parts.
2. Use the `join()` method to concatenate a list of strings into one string.

Feel free to explore the functions provided in this directory for more advanced splitting and joining techniques!