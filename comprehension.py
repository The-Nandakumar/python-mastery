# Comprehension
# A Comprehension is a compact way to create a collection (list, set, or dictionary) from an iterable. 

# List Comprehension
# Syntax: [expression for item in iterable]

devices = ["router", "switch", "firewall"]
names = []
for device in devices:
    names.append(device.upper())

# List comprehension equivalent
names = [device.upper() for device in devices]
print(names)
# Output: ['ROUTER', 'SWITCH', 'FIREWALL']

# with if condition
# [result for item in data if condition]

# with if-else condition
# [result_if_true if condition else result_if_false for item in data]

# Dictionary Comprehension
# Syntax: {key: value for item in iterable}

devices = [
    ("R1", "Router"), 
    ("R2", "Switch"), 
    ("R3", "Firewall")
    ]

device_ips = {name: ip for name, ip in devices}
print(device_ips)
# Output: {'R1': 'Router', 'R2': 'Switch', 'R3': 'Firewall'}

# Set Comprehension
# Syntax: {expression for item in iterable}

interfaces = ["Gig1/0", "Gig1/1", "Gig1/0", "Gig1/2", "Gig1/1"]
unique_interfaces = {interface for interface in interfaces}
print(unique_interfaces)
# Output: {'Gig1/0', 'Gig1/1', 'Gig1/2'}

# Generator Comprehension
# Syntax: (expression for item in iterable)
# Generator comprehension produces values lazily, when requested.
