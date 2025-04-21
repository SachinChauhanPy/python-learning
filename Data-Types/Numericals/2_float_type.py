# 1. Real numbers with decimal points can be positive, negative or zero
a = 3.14
b = -0.001
c = 0.0
print("Positive float:", a)   # Output: Positive float: 3.14
print("Negative float:", b)   # Output: Negative float: -0.001
print("Zero float:", c)       # Output: Zero float: 0.0

# 2. Floats can be written using e or E for scientific notation
d = 1.5e3      # 1.5 * 10^3 = 1500.0
e = 2.5E-4     # 2.5 * 10^-4 = 0.00025
print("Scientific notation (1.5e3):", d)  # Output: 1500.0
print("Scientific notation (2.5E-4):", e) # Output: 0.00025

# 3. Floats have limited precision (~15-17 decimal digits)
f = 0.12345678901234567890
print("Limited precision float:", f)  
# Output: Limited precision float: 0.12345678901234568 (notice rounding at the end)

# 4. Python supports special float values from IEEE 754
inf = float('inf')
ninf = float('-inf')
nan = float('nan')
print("Positive infinity:", inf)    # Output: inf
print("Negative infinity:", ninf)   # Output: -inf
print("Not a number (NaN):", nan)   # Output: nan

# You can also test for these values
import math
print("Is NaN?", math.isnan(nan))           # Output: True
print("Is Infinity?", math.isinf(inf))      # Output: True

# 5. Float comparison issue
x = 0.1 + 0.2
print("0.1 + 0.2 =", x)             # Output: 0.30000000000000004
print("x == 0.3:", x == 0.3)        # Output: False (unexpected!)

# Proper way to compare floats
print("Using math.isclose:", math.isclose(x, 0.3))  # Output: True
