f = open("sample.txt", "r") # Open the file in read mode
data = f.read() # Read the content of the file
print(data)
f.close()
# Output:
# Hello, this is written content.