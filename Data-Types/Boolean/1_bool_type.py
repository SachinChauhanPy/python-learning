# 1. Has only two values: True and False (case-sensitive)
a = True
b = False
print(a, b)
# Output: True False

# true and false (lowercase) are not valid booleans
# true = True  # ✅ OK
# true = true  # ❌ NameError: name 'true' is not defined

# 2. bool is a subclass of int — True is 1, and False is 0
print(int(True), int(False))
# Output: 1 0

print(True + True)  # 1 + 1
# Output: 2

print(False * 10)   # 0 * 10
# Output: 0

# 3. Falsy values — all of these evaluate to False
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(''))      # False
print(bool([]))      # False
print(bool({}))      # False
print(bool(set()))   # False
print(bool(None))    # False
print(bool(False))   # False

# Output:
# False
# False
# False
# False
# False
# False
# False
# False

# 4. Everything else is Truthy
print(bool(1))           # True
print(bool(-1))          # True
print(bool(0.1))         # True
print(bool("hello"))     # True
print(bool([0]))         # True — non-empty list
print(bool({"a": 1}))    # True
print(bool(True))        # True

# Output:
# True
# True
# True
# True
# True
# True
# True
