# 1. Provides zero-copy access to binary data
data = bytearray(b'hello')  # mutable binary data
mv = memoryview(data)
print(mv)
# Output: <memory at 0x...>

# 2. Allows slicing and reading without copying the data
slice_mv = mv[1:4]
print(slice_mv.tobytes())  # Convert view to bytes to see the slice
# Output: b'ell'

# 3. Works with binary types like bytes, bytearray, array.array
readonly = memoryview(b"immutable")  # from bytes (immutable)
print(readonly[0])
# Output: 105 — ASCII for 'i'

# 4. Immutable if source is immutable, mutable if source is mutable
# Trying to change readonly memoryview will raise an error
# readonly[0] = 72  # ❌ TypeError

# But mutable source allows changes
mv[0] = 72  # ASCII for 'H'
print(data)
# Output: bytearray(b'Hello')

# 5. Manipulate data in-place
for i in range(len(mv)):
    mv[i] = mv[i] + 1  # increment each byte value by 1
print(data)
# Output: bytearray(b'Ifmmp') — each character shifted by 1

# 6. Supports slicing and indexing
print(mv[2])       # Indexing
# Output: 109 — ASCII for 'm'

print(mv[1:3].tobytes())  # Slicing
# Output: b'fm'

# 7. Works with structured/multidimensional binary data (e.g., array or numpy)
import array
a = array.array('h', [1000, 2000, 3000])  # 'h' = short integers
mv_arr = memoryview(a)
print(mv_arr[0])
# Output: 1000

# You can slice or modify the data
mv_arr[1] = 2500
print(a)
# Output: array('h', [1000, 2500, 3000])

# 8. Very efficient for passing binary data to functions or I/O operations
# Example simulation: sending a chunk of binary data without copying
def process(chunk):
    print("Processing chunk:", chunk.tobytes())

process(mv[1:4])
# Output: Processing chunk: b'fmm'
