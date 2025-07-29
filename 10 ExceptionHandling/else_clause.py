try:
    print("No error here!")
except:
    print("Error occurred")
else:
    print("Executed only if no exception")
# Output:
# No error here!
# Executed only if no exception

# example:
try: 
    a = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful, result is:", a)
# Output:
# Division successful, result is: 5.0