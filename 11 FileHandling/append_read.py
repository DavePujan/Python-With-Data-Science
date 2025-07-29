f = open("sample.txt", "a+") # Open the file in append and read mode
# This will not overwrite existing content, but allow reading after appending
f.write("Another append.\n") 
f.seek(0)
print(f.read())
f.close()

# Output:
# Another append.
