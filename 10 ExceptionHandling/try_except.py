try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print("An error occurred:", e)