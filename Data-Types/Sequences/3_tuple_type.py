# 1. Immutable and ordered collection of items
my_tuple = (10, 20, 30)
# my_tuple[0] = 99  # ❌ Uncommenting this will raise TypeError: 'tuple' object does not support item assignment
print(my_tuple)  
# Output: (10, 20, 30)

# 2. Tuples can contain duplicate values
duplicates = (1, 2, 2, 3, 1)
print(duplicates)
# Output: (1, 2, 2, 3, 1)

# 3. Tuples use less memory compared to lists
import sys

list_obj = [1, 2, 3]
tuple_obj = (1, 2, 3)

print("List size:", sys.getsizeof(list_obj))  
# Output: List size: <size varies by platform>

print("Tuple size:", sys.getsizeof(tuple_obj))  
# Output: Tuple size: <smaller than list size>

# 4. Faster compared to lists (example: using timeit)
import timeit

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print("List creation time:", list_time)
print("Tuple creation time:", tuple_time)
# Output: Tuple creation time is usually less than list time

# 5. Single element tuple: Needs a trailing comma
single = (5,)
not_a_tuple = (5)

print(type(single))      
# Output: <class 'tuple'>

print(type(not_a_tuple)) 
# Output: <class 'int'>

# 6. Without parentheses: Python allows implicit tuple creation
implicit = 1, 2, 3
print(implicit)
print(type(implicit))
# Output: (1, 2, 3)
#         <class 'tuple'>
