# error_handling_flow.py - Example of error handling flow in Python

def risky_task():
    try:
        print("Trying risky task...")
        x = int("ten")
    except ValueError:
        print("ValueError occurred!")
    else:
        print("No exception occurred.")
    finally:
        print("Task finished.")

risky_task()
# Output:
# Trying risky task...
# ValueError occurred!
# Task finished.
