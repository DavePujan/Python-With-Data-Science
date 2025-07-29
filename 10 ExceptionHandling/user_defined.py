class UnderAgeError(Exception):
    pass

age = 15
try:
    if age < 18:
        raise UnderAgeError("You must be 18+ to vote.")
except UnderAgeError as e:
    print(e)
# Output:
# You must be 18+ to vote.

# pass is used to indicate that no action is taken.