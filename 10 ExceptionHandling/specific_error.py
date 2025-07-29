try:
    lst = [1, 2]
    print(lst[10])
except IndexError as e:
    print("Index error:", e)
# Output:
# Index error: list index out of range

