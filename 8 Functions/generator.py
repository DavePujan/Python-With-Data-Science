# generator.py - Generator using yield

# definition of a generator: A generator is a special type of iterator that allows you to iterate through a sequence of values without storing them all in memory at once.

# what is yield: The yield statement is used to produce a value from a generator function. When the function is called, it returns a generator object that can be iterated over.
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)
