# Strings
# A string (str) is Python's data type for text

#1. Creating a string
# Strings can use single or double quotes
hostname = "Router01"
hostname = 'Router02'

# you can also use triple quotes for multiline text
config = """
interface GigabitEthernet0/1
    description Uplink
    ip address 10.1.1.1 255.255.255.0
    no shutdown
    """

# Strings are immutable, which means you can't modify an existing string
# hostname[0] = "R" #Error will raise
# Instead, python creates a new string
hostname = hostname.upper()
print(hostname)

# 2. Indexing
# You can access individual characters using an index
print(hostname[0])
print(hostname[-3])

# 3. Slicing
# Slicing extracts part of a string
command = "show ip interface brief"
print(command[0:8])

# Output: show ip 
# General syntax
# string[start: stop: step] 
# stop excluded.

text = "abcdef"

print(text[1:4])
text[:4]      # first 4 characters
text[4:]      # from index 4
text[-3:]     # last 3 characters
text[::2]     # every second character

# 4. len()
# returns the number of characters
hostname = "router03"
print(len(hostname))

# Output: 8

# 5. String methods
# 5.1 Case conversion
text.upper()
text.lower()
text.title()
text.capitalize()

# 5.2 Removing whitespace
text.strip()
text.rstrip()
text.lstrip()

output = "    Interface GigabitEthernet0/1      "
output = output.strip()
print(output)

# 5.3 replace()
# Replaces part of a string
# Syntax: string.replace(old, new)
config = "hostname Router1"
config = config.replace("Router1", "Router2")
print(config)

# you can also control how many replacements happen:
text.replace("up","UP",1)

# 5.4 split() and splitlines()
# split() converts a string into a list
command = "show ip interface brief"
words = command.split()
print(words)

# Output: ['show', 'ip', 'interface', 'brief']
# you can specify delimiter
ip = "10.1.1.1"
parts = ip.split(".")
print(parts)

# Output: ['10', '1', '1', '1']

output = """interface Gi0/1
interface Gi0/2
interface Gi0/3"""

lines = output.splitlines()

# Output: 
# [
#     "interface Gi0/1",
#     "interface Gi0/2",
#     "interface Gi0/3"
# ]

# splitlines() is better than split("\n") because splitlines() handles different line-ending conventions properly

# 5.5 join()
# Opposite of split()
# join() combines multiple strings into one string

parts = ["show", "ip", "interface", "brief"]
command = " ".join(parts)
print(command)

# Output: show ip interface brief

interfaces = ["Gi0/1", "Gi0/2", "Gi0/3"]
results = ", ".join(interfaces)
print(results)

# Output: Gi0/1, Gi0/2, Gi0/3

# 5.6 in
# checks whether something exists inside a string
output = "Interface GigabitEthernet0/1 is up"
if "is up" in output:
    print("Interface is operational")

# 5.7 startswith() and endswith()
# Checks how a string begins or ends

interface = "GigabitEthernet0/1"
print(interface.startswith("Giga"))

# Output: True

filename = "router_config.txt"
if filename.endswith(".txt"):
    print("Text file")

# 5.8 find() and index()
# find() used to find the position of text
text = "Interface GigabitEthernet0/1"
position = text.find("GigabitEthernet")
print(position)

# Output: 10
ind = text.index("GigabitEthernet")
print(ind)
# index() raises an exception if it doesn't exist.

# 5.9 count()
# count() tells you how many times something appears
output = """
interface Gi0/1
interface Gi0/2
interface Gi0/3
"""

print(output.count("interface"))

# Output: 3

# 5.10 String validation methods
# Python provides methods that answer questions about the contents of a string
text.isalpha()
text.isdigit()
text.isalnum()
text.isspace()
text.isupper()
text.islower()

# 5.11 partition()
# partition() splits a string into exactly three parts
text = "hostname:router-01"
result = text.partition(":")
print(result)

# Output: ('hostname', ':', 'router-01')
# This can be cleaner than split() when you expect one seperator 

key, separator, value = text.partition(":")
# Why useful: Processing simple key:value formats
