# 1. An immutable version of a set
fs = frozenset([1, 2, 3, 3])
print(fs)
# Output: frozenset({1, 2, 3}) — duplicates removed

# 2. Can be used as a dictionary key or element of another set
my_dict = {frozenset([1, 2]): "A pair"}
print(my_dict)
# Output: {frozenset({1, 2}): 'A pair'}

my_set = {frozenset([1, 2]), frozenset([3, 4])}
print(my_set)
# Output: {frozenset({1, 2}), frozenset({3, 4})}

# 3. Does not maintain insertion order
fs_order = frozenset(["b", "a", "c"])
print(fs_order)
# Output: frozenset({'a', 'b', 'c'}) — order may vary, not guaranteed

# 4. Duplicates are automatically removed
fs_dupes = frozenset([1, 2, 2, 3, 3, 3])
print(fs_dupes)
# Output: frozenset({1, 2, 3})

# 5. Only hashable elements can be in a frozenset
valid_fs = frozenset([(1, 2), "hello", 42])
print(valid_fs)
# Output: frozenset({(1, 2), 'hello', 42})

# invalid_fs = frozenset([[1, 2], 3])  # ❌ This would raise: TypeError: unhashable type: 'list'

# 6. Does not support mutation methods (e.g., add, remove)
# fs.add(4)       # ❌ AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(1)    # ❌ AttributeError: 'frozenset' object has no attribute 'remove'

# Set operations still work
fs2 = frozenset([2, 3, 4])
print(fs.union(fs2))
# Output: frozenset({1, 2, 3, 4})

print(fs & fs2)
# Output: frozenset({2, 3})
