# Creating lists
numbers = [10, 20, 30, 40]
words = ["hello", "world"]
mixed = [1, "apple", 3.14, False]

print("Numbers:", numbers)        # Output: [10, 20, 30, 40]
print("Words:", words)            # Output: ['hello', 'world']
print("Mixed:", mixed)            # Output: [1, 'apple', 3.14, False]

# Indexing and slicing
print("First number:", numbers[0])       # Output: 10
print("Last number:", numbers[-1])       # Output: 40
print("Slice (1:3):", numbers[1:4    ])      # Output: [20, 30]

# Mutability
numbers[2] = 99
print("After change:", numbers)          # Output: [10, 20, 99, 40]

# Adding elements
numbers.append(50)
print("After append:", numbers)          # Output: [10, 20, 99, 40, 50]
numbers.insert(1, 15)
print("After insert:", numbers)          # Output: [10, 15, 20, 99, 40, 50]

# Removing elements
numbers.remove(99)
print("After remove 99:", numbers)       # Output: [10, 15, 20, 40, 50]
popped = numbers.pop(2)
print("Popped element:", popped)         # Output: 20
print("After pop:", numbers)             # Output: [10, 15, 40, 50]
del numbers[0]
print("After delete:", numbers)          # Output: [15, 40, 50]

# Membership test
print("Is 40 in list?", 40 in numbers)   # Output: True

# Looping
print("Looping through list:")
for n in numbers:
    print(n)
# Output:
# 15
# 40
# 50

# Built-in functions
nums = [4, 1, 7, 3]
print("Sorted:", sorted(nums))           # Output: [1, 3, 4, 7]
nums.sort()
print("After sort:", nums)               # Output: [1, 3, 4, 7]
nums.reverse()
print("After reverse:", nums)            # Output: [7, 4, 3, 1]

# Nested list
matrix = [[1, 2], [3, 4]]
print("Element at [1][0]:", matrix[1][0])  # Output: 3
