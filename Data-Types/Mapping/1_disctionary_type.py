# 1. Dictionary definition using {}
person = {"name": "Alice", "age": 25}
print(person)
# Output: {'name': 'Alice', 'age': 25}

# 2. Keys are unique — duplicate keys will overwrite previous value
dup_key_dict = {"a": 1, "b": 2, "a": 3}
print(dup_key_dict)
# Output: {'a': 3, 'b': 2} — 'a' is overwritten

# 3. Keys must be immutable — valid: str, int, tuple (if hashable)
valid_dict = {
    "string": "ok",
    123: "int key",
    (1, 2): "tuple key"
}
print(valid_dict)
# Output: {'string': 'ok', 123: 'int key', (1, 2): 'tuple key'}

# 4. Values can be any data type
mixed_values = {
    "list": [1, 2, 3],
    "dict": {"x": 1},
    "bool": True,
    "function": len
}
print(mixed_values["list"])
# Output: [1, 2, 3]

# 5. Mutable — Add, update, remove items
person["city"] = "New York"  # Add new key
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

person["age"] = 26  # Update existing value
print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

del person["city"]  # Delete key
print(person)
# Output: {'name': 'Alice', 'age': 26}

# 6. Insertion order is preserved (Python 3.7+)
ordered_dict = {}
ordered_dict["first"] = 1
ordered_dict["second"] = 2
ordered_dict["third"] = 3
print(ordered_dict)
# Output: {'first': 1, 'second': 2, 'third': 3}

# 7. Access value
print(person["name"])
# Output: Alice

# 8. Safe access with .get() (avoids KeyError)
print(person.get("age"))       # Existing key
# Output: 26
print(person.get("city"))      # Non-existing key
# Output: None

# 9. Check if key exists
print("name" in person)
# Output: True
print("city" in person)
# Output: False

# 10. Iterating through dictionary
for key in person:
    print(key, "=>", person[key])
# Output:
# name => Alice
# age => 26

for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 26

# 11. Dictionary methods
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 26])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 26)])

# 12. pop() and clear()
popped = person.pop("age")
print(popped)
# Output: 26
print(person)
# Output: {'name': 'Alice'}

person.clear()
print(person)
# Output: {}

# 13. update() — merge or modify values
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)
# Output: {'a': 1, 'b': 3, 'c': 4}
