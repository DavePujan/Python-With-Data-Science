f = open("sample.txt", "r+") # Open the file in read and write mode
# This will allow reading and writing without truncating the file

print("Before:", f.read()) # Read the current content
f.seek(0)
f.write("Updated from r+\n") # This will overwrite the beginning of the file
f.close()
# Output:
# Before: Hello, this is written content.
