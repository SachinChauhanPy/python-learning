# 1. Complex numbers with real and imaginary parts
z = 2 + 3j  # Python uses 'j' for the imaginary unit
print("Complex number z:", z)  
# Output: (2+3j)

# 2. In 2 + 3i, ‘2’ and ‘3’ are real numbers, and ‘i’ is the imaginary unit
# In Python, this is written as 2 + 3j

# 3. Access real and imaginary parts
print("Real part:", z.real)  # Output: 2.0
print("Imaginary part:", z.imag)  # Output: 3.0

# 4. Cannot compare complex numbers
z1 = 2 + 3j
z2 = 1 + 4j

# print(z1 > z2)  # ❌ This will raise: TypeError: '>' not supported between instances of 'complex' and 'complex'

print("Attempting to compare z1 > z2 will raise a TypeError.")  # Just to explain
