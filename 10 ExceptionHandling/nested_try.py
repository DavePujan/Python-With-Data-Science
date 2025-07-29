try:
    print("Outer try block")
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Handled in inner try")
except:
    print("Handled in outer try")
# Output:
# Outer try block
# Handled in inner try
