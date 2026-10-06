# Lambda Functions
# Lambda functions in python is a small anonymous (unnamed) function that you can define in a single line.
# It's mainly used for short, simple operations where writing a function with def would feel unnecessary.

# SYNTAX:
# lambda arguments: expression

# Simple example

add = lambda a, b: a + b
print(add(10, 20))

# Output: 30

# It can have any number of arguments but only one expression. The expression is evaluated and returned automatically.

# When to Use (and Not Use)
# 	Use lambda when:
# 		• The function is very short 
# 		• You need it temporarily 
# 		• It improves readability in-place 
# 	Avoid lambda when:
# 		• The logic is complex 
# 		• You need multiple steps or statements 
#       • Readability suffers

# map
# map() applies the same function to every item in an iterable
# map(function, iterable)

ips = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]
def get_last_octet(ip):
    return ip.split(".")[-1]
result = map(get_last_octet, ips)
print(list(result))

# output ['1', '2', '3']

# with lambda
ips = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]
result = list(map(lambda ip: ip.split(".")[-1], ips))
print(result)

# filter
# filter() keeps only the the items that satisfy a condition
# filter(function, iterable)
# The function must return True or False

ips = [
    "10.1.1.1",
    "10.1.1.2",
    "192.168.1.1",
    "10.1.1.3"
]
def is_management_ip(ip):
    return ip.startswith("10.1.")
result = filter(is_management_ip, ips)
print(list(result))

# Output ['10.1.1.1', '10.1.1.2', '10.1.1.3']

# with lambda
ips = ["10.1.1.1", "192.168.1.1", "10.1.1.2"]
result = list(filter(lambda ip: ip.startswith("10.1."), ips))
print(result)

# reduce
# reduce() repeatedly combines items to produce one final value
# it comes from functools:
from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda x, y: x + y, numbers)
print(result)

# output - 100
# conceptually
# 10 + 20 = 30
# 30 + 30 = 60
# 60 + 40 = 100
# reduce = combine many items into one result