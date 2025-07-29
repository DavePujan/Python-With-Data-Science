# this file checks if a file exists in the current directory.
# if file exists, it prints "File exists." Otherwise, it prints "File does not exist."


import os
file = "sample.txt"
if os.path.exists(file):
    print("File exists.")
else:
    print("File does not exist.")
