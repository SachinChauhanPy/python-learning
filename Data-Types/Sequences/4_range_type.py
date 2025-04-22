# 1. Returns an immutable sequence of numbers
r = range(5)  # Creates a range object from 0 to 4
print(r)
# Output: range(0, 5)

print(type(r))  # Checking the type of the object
# Output: <class 'range'>

# 2. Three ways to create a range

# a) range(stop) — starts at 0, ends before stop
print(list(range(5)))  # Converts range to a list for display
# Output: [0, 1, 2, 3, 4]

# b) range(start, stop) — starts at 'start', ends before 'stop'
print(list(range(2, 7)))  # Starts at 2, ends at 6
# Output: [2, 3, 4, 5, 6]

# c) range(start, stop, step) — with a step value
print(list(range(10, 2, -2)))  # Counts down by 2s from 10 to just above 2
# Output: [10, 8, 6, 4]

# 3. Cannot be changed after creation (immutable)
# Attempting to change an element will raise an error
# r[0] = 100  # ❌ This line would raise: TypeError: 'range' object does not support item assignment

# 4. Uses minimal memory regardless of size
import sys

small_range = range(10)        # Small range
large_range = range(1000000)   # Very large range

print("Size of small_range:", sys.getsizeof(small_range))  # Check memory size
# Output: Size of small_range: 48 (may vary by system)

print("Size of large_range:", sys.getsizeof(large_range))  # Same memory usage!
# Output: Size of large_range: 48 (very memory efficient)

# 5. Can be converted to list or tuple
print(list(range(3)))  # Convert to list
# Output: [0, 1, 2]

print(tuple(range(3)))  # Convert to tuple
# Output: (0, 1, 2)

# 6. Supports slicing and indexing like a list
r2 = range(10)

print(r2[2])  # Indexing: get value at index 2
# Output: 2

print(r2[2:7])  # Slicing: get range object from index 2 to 6
# Output: range(2, 7)

print(list(r2[2:7]))  # Convert sliced range to list for display
# Output: [2, 3, 4, 5, 6]
