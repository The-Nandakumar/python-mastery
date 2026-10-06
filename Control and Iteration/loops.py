# Loops in Python
# 1. for
# 2. while

# 1. for loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

devices = ["R1", "R2", "R3", "R4"]
for device in devices:
    print(device)

# Network example:
ip_addresses = ["10.1.1.1","10.1.1.2","10.1.1.3"]
for ip in ip_addresses:
    print(ip)

# Iterating through a string
for char in "Python":
    print(char)

# Output: P, y, t, h, o, n

# Iterating through a dictionary
devices = {
    "hostname": "R1",
    "ip": "10.1.1.1",
    "vendor": "Cisco"
}

# Keys
for key in devices:
    print(key)
# Output: hostname, ip, vendor

# Values
for value in devices.values():
    print(value)
# Output: R1, 10.1.1.1, Cisco

# Key-Value pairs
for key, value in devices.items():
    print(f"{key}: {value}")
# Output: hostname: R1
#         ip: 10.1.1.1
#         vendor: Cisco

# for ... else
# The else runs when the loop completes without hitting a break statement.
devices = ["R5", "R6", "R7", "R8"]
for device in devices:
    print(device)
else:
    print("Loop completed without hitting a break statement.")

# Same concept applies to while loops as well.

# Nested loops
# A nested loop is a loop inside another loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
devices = ["R9", "R10"]
interfaces = ["Gig1/0", "Gig1/1"]
for device in devices:
    for interface in interfaces:
        print(f"{device}: {interface}")
# Output:
# R9: Gig1/0
# R9: Gig1/1
# R10: Gig1/0
# R10: Gig1/1

# Looping through a list of dictionaries
devices = [
    {"hostname": "R1", "ip": "10.1.1.1"},
    {"hostname": "R2", "ip": "10.1.1.2"},
    {"hostname": "R3", "ip": "10.1.1.3"}
]
for device in devices:
    print(f"{device['hostname']}: {device['ip']}")
# Output:
# R1: 10.1.1.1
# R2: 10.1.1.2
# R3: 10.1.1.3

# 2. while loop
# A while loop keeps executing as long as a condition is true.
attempt = 0
while attempt < 3:
    print("Trying to connect...")
    attempt += 1

# Difference between for and while loop:
# for    → usually iterate over a known collection
# while  → repeat based on a condition

# 3. range()
# To loop through a set of code a specified number of times, we can use the range() function.
# A range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(5):
    print(i)

# output:
# 0
# 1
# 2
# 3
# 4

# Notice that 5 is not included.

# Three forms
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(1,6):
    print(i)

# Output: 1, 2, 3, 4, 5

for i in range(1, 10, 2):
    print(i)

# Output: 1, 3, 5, 7, 9

# 4. enumerate()
# This is one of the most useful built-in functions in Python when we want both the index and the value of an iterable object.
interfaces = ["Gig0/0", "Gig0/1", "Gig0/2"]
for index, interface in enumerate(interfaces):
    print(f"Interface {index}: {interface}")

# Output:
# Interface 0: Gig0/0
# Interface 1: Gig0/1
# Interface 2: Gig0/2

# Suppose we want to start the index from 1 instead of 0, we can use the start parameter of the enumerate() function.
interfaces = ["Gig0/0", "Gig0/1", "Gig0/2"]
for index, interface in enumerate(interfaces, start=1):
    print(f"Interface {index}: {interface}")

# Output:
# Interface 1: Gig0/0
# Interface 2: Gig0/1
# Interface 3: Gig0/2

# 5. zip()
# zip function takes multiple lists or other data collections and returns an iterator of tuples, 
# where the first item in each passed iterator is paired together, and then the second item in each passed iterator is paired together, and so on.
# If one list is shorter than the other, it will stop when the shortest list is exhausted.
hostnames = ["R1", "R2", "R3"]
ip_addresses = ["10.1.1.1", "10.1.1.2", "10.1.1.3"]
for hostname, ip in zip(hostnames, ip_addresses):
    print(f"{hostname}: {ip}")

# Output:
# R1: 10.1.1.1
# R2: 10.1.1.2
# R3: 10.1.1.3

# 6. break
# The break statement immediately exits the loop.
devices = ["R1", "R2", "R3", "R4"]
for device in devices:
    if device == "R3":
        break
    print(device)

# Output:
# R1
# R2

# 7. continue
# The continue statement skips the current iteration and moves to the next iteration of the loop.
devices = ["R1", "R2", "R3", "R4"]
for device in devices:
    if device == "R2":
        continue
    print(device)

# Output: 
# R1
# R3
# R4


# 8. pass
# The pass statement is used as a placeholder for future code. 
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
for device in devices:
    pass  # Placeholder for future code
