# Tuple
# A tuple is an ordered collection of values, similar to a list, but immutable

router = ("R1", "10.1.1.1", 22)
print(router)
print(router[0])
print(router[1])

# Output
# ('R1', '10.1.1.1', 22)
# R1
# 10.1.1.1

# In production code, tuples are commonly used for fixed structures, function return values, configuration-like data, and dictionary keys

# Tuple indexing exactly like lists
devices = ("R1", "R2", "R3", "R4")

print(devices[0])    # R1
print(devices[2])    # R3
print(devices[-1])   # R4

# Tuple slicing
devices = ("R1", "R2", "R3", "R4")

print(devices[1:3])
print(devices[:2])      # ('R1', 'R2')
print(devices[2:])      # ('R3', 'R4')
print(devices[::-1])    # ('R4', 'R3', 'R2', 'R1')

# Tuples are immutable so you can' modify its position, also you can't
# devices.append("R4")
# devices.remove("R2")
# devices.sort()

# Tuple methods
# 1. count()
# Counts how many times a value appears
interfaces = ("Gi0/1", "Gi0/2", "Gi0/1", "Gi0/3")
print(interfaces.count("Gi0/1"))

# Output: 2

# 2. index()
# Returns the index of the first occurrence
interfaces = ("Gi0/1", "Gi0/2", "Gi0/1", "Gi0/3")
print(interfaces.index("Gi0/1"))

# Output: 0
x = interfaces.index("Gi0/1", 1) #Start searching from index 1.
print(x)

# Output: 2

# Tuples unpacking
# Suppose,
router = ("R1", "10.1.1.1", 22)

# instead of,
name = router[0]
ip = router[1]
port = router[2]

# We can
name, ip, port = router

# This is called iterable unpacking.It isn't limited to tuples
a, b = [10, 20]

# Extended unpacking
interfaces = ("Gi0/1", "Gi0/2", "Gi0/3", "Gi0/4")
first, *remaining = interfaces
print(first)
print(remaining)

# Output
# Gi0/1
# ['Gi0/2', 'Gi0/3', 'Gi0/4']
# remaining is a list, not a tuple.

# Tuple concatenation
# You can combine tuples using +
a = ("R1", "R2")
b = ("R3", "R4")

c = a + b

print(c)

# Output ('R1', 'R2', 'R3', 'R4')
# The above is a new tuple

# Tuple repetition
# You can use *
x = ("R1",) * 3
print(x)

# Output ('R1', 'R1', 'R1')

# Membership testing
# Use in and not in
devices = ("R1", "R2", "R3")
print("R2" in devices)
# Output: True
print("R10" not in devices)
# Output: True

# Nested tuples
routers = (
    ("R1", "10.1.1.1"),
    ("R2", "10.1.1.2"),
    ("R3", "10.1.1.3")
)

print(routers[0])
print(routers[0][1])

# Output
# ('R1', '10.1.1.1')
# 10.1.1.1

# Tuples built-in Functions
# 1. len()
devices = ("R1", "R2", "R3")
print(len(devices))

# Output: 3

# 2. min()/ max()
numbers = (10, 20, 5, 30)
print(min(numbers))  # 5
print(max(numbers))  # 30

# sum()
numbers = (10, 20, 30)
print(sum(numbers)) # 60

# sorted()
# It doesn't modify the tuple

numbers = (30, 10, 20)
result = sorted(numbers)
print(result) #[10, 20, 30]