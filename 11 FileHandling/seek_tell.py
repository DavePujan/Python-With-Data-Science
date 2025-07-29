f = open("sample.txt", "r")
print("Initial Position:", f.tell())
data = f.read(5)
print("After reading 5 chars:", f.tell())
f.seek(0)
print("After seek to start:", f.read())
f.close()
# Output:
# Initial Position: 0
# After reading 5 chars: 5
# After seek to start: Hello, this is written content.

# This code demonstrates the use of `seek` and `tell` methods in file handling.
