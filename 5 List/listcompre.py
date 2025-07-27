# listcompre.py - List Comprehension

squares = [x*x for x in range(1, 6)]
print("Squares:", squares)  # [1, 4, 9, 16, 25]

evens = [x for x in range(1, 11) if x % 2 == 0]
print("Evens:", evens)  # [2, 4, 6, 8, 10]