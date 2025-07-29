# return.py - Function with return value

def add(a, b):
    return a + b

result = add(3, 4)
print("Sum =", result)


# without return
def add_without_return(a, b):
    print("Sum =", a + b)

add_without_return(3, 4)  # This will print the sum but not return it
# Output: Sum = 7