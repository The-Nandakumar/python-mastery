# Sets
# A set is a collection used to store unique values.
# Sets are very useful in real applications when you care about membership, uniqueness, and comparing collections.
# For example, in network automation, you may have a list of IP addresses discovered from multiple sources and want only unique IPs.

# 1. Creating a set
# Use {} or set()
devices = {"R1", "R2", "R3"}
print(devices) # {'R2', 'R3', 'R1'}
set_devices = set(["R1", "R2", "R3"])
print(set_devices) # {'R2', 'R3', 'R1'}

# 2. Characteristic of Sets
# Unordered
# Don't allow duplicate
# You can't put immutable objects into set

# 3. empty set
x = set() # not x = {}

# 4. Adding elements
devices.add("R4")
# If the element already exists, nothing happens

# 5. Adding multiple elements

devices.update(["R5", "R6"])
print(devices) # {'R6', 'R1', 'R3', 'R4', 'R5', 'R2'}

# 6. Removing elements
# 6.1 remove()
devices.remove("R2")
# if the element doesn't exist, it will raise a error

# 6.2 discard()
devices.discard("R1")
# If the element doesn't exist, nothing happens

# 6.3 pop()
device = devices.pop()
print(device)
# It removes and returns an arbitrary element.
# Don't assume it removes the first or last element.

# 7. clear()
# Removes everything
devices.clear()
print(devices) # set()

# 8. Set Operations
cisco = {"R1", "R2", "R3"}
juniper = {"R3", "R5", "R6"}

# 8.1 Union
# Everything from both sets
union = cisco | juniper
print(union) # {'R3', 'R6', 'R5', 'R4', 'R1', 'R2'}

# 8.2 Intersection
# Elements presents in both sets
intersection = cisco & juniper
print(intersection) # {'R3'}

# 8.3 Difference
# Elements that exist in the first set but not in the second
diff = cisco - juniper
print(diff) # {'R2', 'R1'}

# 8.4 Symmetric difference
# Elements that exist in either set, bit not both
sym_diff = cisco ^ juniper
print(sym_diff) # {'R2', 'R5', 'R6', 'R1'}

# 8.5 Subset and Superset
all_devices = {"R1", "R2", "R3", "R4"}
branch_devices = {"R1", "R2"}

branch_devices.issubset(all_devices)
# True
all_devices.issuperset(branch_devices)
# True

# 8.6 Disjoint Sets
# isdisjoint()
# checks whether two sets have no common elements

set1 = {"R1", "R2"}
set2 = {"R3", "R4"}
print(set1.isdisjoint(set2)) # True

# 9. copy()
devices = {"R6", "R7", "R8"}
backup = devices.copy()

# now backup is a separate set

# Fronzen set
# A fronzen set cannot be changed
devices.add("R3")
devices = frozenset({"R1","R2"})
# devices.add("R3") # This wont work/*