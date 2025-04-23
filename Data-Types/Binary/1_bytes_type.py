# 1. Bytes is an immutable sequence of integers in the range 0 to 255
b = bytes([65, 66, 67])  # ASCII codes for A, B, C
print(b)
# Output: b'ABC'

# 2. It represents binary data, like images, files, or network streams
# (We'll simulate this with a bytes object)
binary_data = b'\x89PNG\r\n\x1a\n'
print(binary_data)
# Output: b'\x89PNG\r\n\x1a\n' — binary header of a PNG file

# 3. Can create bytes using b'' or bytes([...])
b1 = b'hello'
b2 = bytes([104, 101, 108, 108, 111])
print(b1)
# Output: b'hello'
print(b2)
# Output: b'hello'

# 4. Each element is an integer (0–255), not characters
print(b1[0])
# Output: 104 — ASCII code for 'h'

# 5. Supports indexing and slicing like lists and strings
print(b1[1])      # Second byte
# Output: 101 — ASCII code for 'e'

print(b1[1:4])    # Slice
# Output: b'ell'
