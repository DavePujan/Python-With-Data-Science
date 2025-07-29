f = open("sample.txt", "a") # Open the file in append mode
# This will not overwrite existing content, but add to it

f.write("Appending this line.\n")
f.close()

# Output:
# Appending this line.