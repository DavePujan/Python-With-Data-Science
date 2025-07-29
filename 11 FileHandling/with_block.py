# with definition: A generator is a special type of iterator that allows you to iterate through a sequence of values without storing them all in memory at once.

# it will be used in the context of file handling to read large files efficiently.

with open("sample.txt", "r") as f:
    print(f.read())
# No need to manually close
