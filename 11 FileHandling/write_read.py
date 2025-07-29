f = open("sample.txt", "w+") # Open the file in write and read mode
# This will create the file if it doesn't exist or overwrite it if it does
f.write("Writing then reading.\n")
f.seek(0) # Move the cursor to the beginning of the file
print("Content of the file after writing:")
print(f.read())
f.close()

# Output:
# Content of the file after writing:
# Writing then reading.
# Writing then reading.