# immutable.py - Tuple immutability

t = (1, 2, 3)
# t[0] = 99  # ❌ TypeError
print("Tuple is immutable:", t)
# t.append(4)  # ❌ AttributeError
print("Cannot modify tuple:", t)
# t.pop()  # ❌ AttributeError
print("No methods to modify:", t)
# t.remove(2)  # ❌ AttributeError
print("No removal methods:", t)
# t.clear()  # ❌ AttributeError
print("No clear method:", t)
# t.extend([4, 5])  # ❌ AttributeError
print("No extend method:", t)
# t.insert(1, 99)  # ❌ AttributeError
print("No insert method:", t)
# t.sort()  # ❌ AttributeError
print("No sort method:", t)
# t.reverse()  # ❌ AttributeError
print("No reverse method:", t)
# t.remove(1)  # ❌ AttributeError
print("No remove method:", t)