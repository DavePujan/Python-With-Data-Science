# Writing binary
with open("binary.dat", "wb") as f: # Open the file in binary write mode
    f.write(b'\x41\x42\x43')

# Reading binary
with open("binary.dat", "rb") as f: # Open the file in binary read mode
    print(f.read())
# Output:
# b'ABC'

# This code demonstrates how to write and read binary data in Python.
# the code uses the `wb` mode for writing binary data and `rb` mode for reading it. The output shows the binary content read from the file.