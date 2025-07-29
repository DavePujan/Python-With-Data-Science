# all_methods.py - Dictionary methods overview

d = {"a": 1, "b": 2}
print("get:", d.get("a"))
print("keys:", list(d.keys()))
print("values:", list(d.values()))
print("items:", list(d.items()))
print("pop:", d.pop("a"))
print("copy:", d.copy())
print("clear:", d.clear())
print("update:", d.update({"c": 3}))
print("popitem:", d.popitem())
print("setdefault:", d.setdefault("d", 4))
