# 1. A string is a sequence of characters
text = "Hello 123! 😊"
print("Original string:", text)  
# Output: Original string: Hello 123! 😊

# We can loop through the sequence
print("Characters in the string:")
for char in text:
    print(char, end=" ")  
# Output: H e l l o   1 2 3 ! 😊
print("\n")

# 2. Strings are immutable
immutable = "hello"
# immutable[0] = 'H'  # ❌ TypeError: 'str' object does not support item assignment
print("Trying to modify a string will raise an error (strings are immutable)")
# Output: Trying to modify a string will raise an error (strings are immutable)

# 3. Strings can be defined using single, double, or triple quotes
single_quoted = 'Hello'
double_quoted = "World"
multiline = '''This is
a multiline
string.'''

print("Single quoted:", single_quoted)     
# Output: Single quoted: Hello
print("Double quoted:", double_quoted)     
# Output: Double quoted: World
print("Multiline string:\n", multiline)
# Output: 
# Multiline string:
# This is
# a multiline
# string.

# 4. Cannot concatenate string with other types directly
age = 25
# print("Age is " + age)  # ❌ TypeError
print("Age is " + str(age))  
# Output: Age is 25

# 5. f-strings (Python 3.6+)
name = "Alice"
score = 95.5
print(f"{name} scored {score} marks.")  
# Output: Alice scored 95.5 marks.

# ✅ Handy string tricks:

# a. Strip whitespace
messy = "   hello world   "
print("Stripped:", messy.strip())  
# Output: Stripped: hello world

# b. Replace parts of a string
sentence = "I love apples"
print("Replace apples with oranges:", sentence.replace("apples", "oranges"))  
# Output: Replace apples with oranges: I love oranges

# c. Count characters
print("Number of 'l's in 'hello':", "hello".count("l"))  
# Output: Number of 'l's in 'hello': 2

# d. Check membership
print("'lo' in 'hello'?", "lo" in "hello")  
# Output: 'lo' in 'hello'? True

# e. Split and join
csv = "one,two,three"
parts = csv.split(",")  
# parts = ['one', 'two', 'three']
joined = "-".join(parts)  
# joined = 'one-two-three'
print("Split:", parts)  
# Output: Split: ['one', 'two', 'three']
print("Joined:", joined)  
# Output: Joined: one-two-three

# f. Title case and capitalization
title = "python is fun"
print("Title case:", title.title())    
# Output: Title case: Python Is Fun
print("Capitalized:", title.capitalize())  
# Output: Capitalized: Python is fun

# g. Reverse a string
reversed_text = text[::-1]
print("Reversed string:", reversed_text)  
# Output: Reversed string: 😊 !321 olleH
