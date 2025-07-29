# global.py - Global variable example

x = 10 # global variable

def update():
    global x
    x = 20

update()
print("x =", x)
# Output: x = 20