try:
    a = int("hello")
    b = 10 / 0
except ValueError:
    print("Value Error occurred")
except ZeroDivisionError:
    print("Division by zero!")
except Exception as e:
    print("An unexpected error occurred:", e)