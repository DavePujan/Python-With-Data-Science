# slicing.py - Tuple slicing

t = (10, 20, 30, 40, 50)
print("Slice [1:4]:", t[1:4])  # (20, 30, 40)
print("Slice [:3]:", t[:3])    # (10, 20, 30)
print("Slice [2:]:", t[2:])    # (30, 40, 50)
print("Slice [-3:]:", t[-3:])  # (30,  40, 50)
print("Slice [::2]:", t[::2])  # (10, 30, 50)
print("Slice [1::2]:", t[1::2])  # (20, 40)