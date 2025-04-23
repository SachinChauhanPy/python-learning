# 1. Unordered collection of unique and immutable (hashable) elements
example_set = {1, 2, 3, "apple", (4, 5)}
print(example_set)
# Output: Set with unique elements, e.g., {1, 2, 3, 'apple', (4, 5)} (order may vary)

# 2. Automatically removes duplicate values
dup_set = {1, 2, 2, 3, 3, 3}
print(dup_set)
# Output: {1, 2, 3}

# 3. No index, no order — elements may appear in any sequence
# print(dup_set[0])  # ❌ This would raise: TypeError: 'set' object is not subscriptable

# 4. You can add or remove elements
dup_set.add(4)        # Add new element
dup_set.remove(2)     # Remove existing element
print(dup_set)
# Output: {1, 3, 4} (order may vary)

# 5. Only hashable elements can be in a set
# invalid_set = {1, [2, 3]}  # ❌ This will raise: TypeError: unhashable type: 'list'

valid_set = {(1, 2), "hello", 42}
print(valid_set)
# Output: {(1, 2), 'hello', 42} (order may vary)

# 6. Membership tests are fast
my_list = list(range(100000))
my_set = set(my_list)

import time

# Test with list
start = time.time()
found = 99999 in my_list
end = time.time()
print("List membership test time:", end - start)
# Output: Slower

# Test with set
start = time.time()
found = 99999 in my_set
end = time.time()
print("Set membership test time:", end - start)
# Output: Much faster
