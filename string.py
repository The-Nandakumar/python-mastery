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

# 5.4 split()
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

# 5.5 join()