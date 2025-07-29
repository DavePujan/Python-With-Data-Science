f = open("sample.txt", "r")
lines = f.readlines() # Read all lines from the file
print("Content of the file:")
for line in lines:
    print(line.strip())
f.close()

# Output:
# Content of the file: 
# Hello, this is written content.
