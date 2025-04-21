# 1. Positive or a negative number without any decimal point
a = 42       # Positive integer
b = -17      # Negative integer
print("Positive int:", a) # Output - > Positive int: 42
print("Negative int:", b) # Output - > Negative int: -17

# 2. Python's int supports arbitrarily large numbers
big_number = 1234567890123456789012345678901234567890
print("Big number:", big_number) 
# Output - > Big number: 1234567890123456789012345678901234567890

# 3. No overflow error - automatic conversion to long int
huge = 2 ** 1000  # This would overflow in many languages
print("2 ** 1000 =", huge)
# Output - > 2 ** 1000 = 107150860718626732094842504906000181056140481170553360744375038837035105112493612249319837881569585812759467291...

# 4. Boolean behavior of integers
print("bool(0):", bool(0))       # Output - > False
print("bool(42):", bool(42))     # Output - > True
print("bool(-1):", bool(-1))     # Output - > True