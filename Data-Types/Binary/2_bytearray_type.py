# 1. A mutable sequence of integers in the range 0 to 255
ba = bytearray([65, 66, 67])  # A, B, C
print(ba)
# Output: bytearray(b'ABC')

# 2. Represents binary data, just like bytes, but can be modified in place
ba[0] = 90  # Change 'A' (65) to 'Z' (90)
print(ba)
# Output: bytearray(b'ZBC')

# 3. Can create bytearrays using bytearray([int, int, ...]) or bytearray(b'some bytes')
ba1 = bytearray([100, 101, 102])
print(ba1)
# Output: bytearray(b'def')

ba2 = bytearray(b'hello')
print(ba2)
# Output: bytearray(b'hello')

# 4. Can specify encoding for the string we have given
ba3 = bytearray("world", "utf-8")
print(ba3)
# Output: bytearray(b'world')

# 5. Elements can be changed, added, or removed
ba3[0] = 87  # Change 'w' to 'W'
print(ba3)
# Output: bytearray(b'World')

ba3.append(33)  # Add '!' (ASCII 33)
print(ba3)
# Output: bytearray(b'World!')

ba3.pop()
print(ba3)
# Output: bytearray(b'World')

# 6. Supports indexing, slicing, and assignment
print(ba3[1])      # Indexing
# Output: 111 (ASCII for 'o')

print(ba3[1:4])    # Slicing
# Output: bytearray(b'orl')

ba3[1:4] = b"XYZ"  # Assignment
print(ba3)
# Output: bytearray(b'WXYZd')

# 7. Like bytes, each element is an integer from 0 to 255
print([i for i in ba3])
# Output: [87, 88, 89, 90, 100]

# 8. Efficient for binary I/O operations where in-place changes are needed
# (Example: altering file content without reloading the entire file into memory)
# We'll simulate it:
binary_chunk = bytearray(b'\x00\x01\x02\x03')
binary_chunk[2] = 255  # Modify in-place
print(binary_chunk)
# Output: bytearray(b'\x00\x01\xff\x03')
