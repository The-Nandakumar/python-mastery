# A dictionary is a collection that stores data as key-value pairs

# Creating a dictionary
router = {}

# with data
router = {
    "hostname" : "R1",
    "ip" : "10.1.1.1",
    "vendor" : "Cisco"
}

# also can use
router = dict(
    hostname = "R1",
    ip = "10.1.1.1",
    vendor = "Cisco"
)

# A dictionary can contain different data types as values
device = {
    "hostname": "R1",
    "ip": "10.1.1.1",
    "ssh_port": 22,
    "interfaces": ["Gi0/0", "Gi0/1"],
    "management_enabled": True
}

# Dictionary keys must he unique
router = {
    "hostname": "R1",
    "hostname": "R2"
}

print(router) # {'hostname': 'R2'}
# Second value replaces the first one
# value can be repeatable

# Dictionary keys must be Hashable
# Hashable - 
# Common valid keys
data = {
    "hostname": "R1",
    1: "one",
    (10, 20): "coordinates"
}
# But a list cannot
# data = {
#     ["hostname"]: "R1"
# }

# Accessing a dictionary
router = {
    "hostname": "R1",
    "ip": "10.1.1.1"
}

print(router["hostname"]) # R1
# better use get() because when key doesn't exist it wont throw you an error

# get()
# syntax
# dictionary.get(key)
# or
# dictionary.get(key, default_value)

router = {
    "hostname": "R1",
    "ip": "10.1.1.1"
}

print(router.get("hostname")) # R1
print(router.get("username")) # None
print(router.get("username", "admin")) # admin

# why get useful?
# Suppose you're processing device data from an API (example above router dictionary), some devices don't have "location". so, 
# location = device["location"]  # KeyError
# We can use
location = device.get("location", "Unknown")

# Adding and Updating values
router["vendor"] = "Juniper"
print(router) # {'hostname': 'R1', 'ip': '10.1.1.1', 'vendor': 'Juniper'}

router["ip"] = "20.1.1.1"
print(router) # {'hostname': 'R1', 'ip': '20.1.1.1', 'vendor': 'Juniper'}

# update()
# you can update mutliple values at once
router.update({
    "ip" : "30.1.1.1",
    "vendor" : "Arista",
    "port" : 22
})
print(router) # {'hostname': 'R1', 'ip': '30.1.1.1', 'vendor': 'Arista', 'port': 22}

# Removing dictionary Items
# pop()
port = router.pop("port")
print(port) # 22
print(router) # {'hostname': 'R1', 'ip': '30.1.1.1', 'vendor': 'Arista'}

# you can also provide a default value
router.pop("Location", "Not found")

# del
del router["vendor"]
print(router) # {'hostname': 'R1', 'ip': '30.1.1.1'}

# Difference between pop and delete is pop() removes it and gives you the removed value where del simply removes it. 
# If the key doesn't exist, both can cause an error, although pop() can avoid that with a default.

# clear()
# Removes everything from the dictionary
router.clear()
print(router) # {}

# To get key and value
for key in router.keys():
    print(key)

for value in router.values():
    print(value)

for key, value in router.items():
    print(key, value)

# Checking whether a key exists
# Use in
router = {
    "hostname": "R1",
    "ip": "10.1.1.1"
}

if "hostname" in router:
    print("Hostname exists")

# if you want to check the values
if "R1" in router.values():
    print("Router name is R1")

# len()
print(len(router)) # 2

# Nested Dictionaries
network = {
    "router1": {
        "ip": "10.1.1.1",
        "vendor": "Cisco"
    },
    "router2": {
        "ip": "10.1.1.2",
        "vendor": "Juniper"
    }
}

print(network["router1"]["ip"]) # 10.1.1.1

# Dictionary + List
router = {
    "hostname": "R1",
    "interfaces": [
        "GigabitEthernet0/0",
        "GigabitEthernet0/1"
    ]
}

print(router["interfaces"][1]) # GigabitEthernet0/1

# Merging dictionary
router_info = {
    "hostname": "R1",
    "ip": "10.1.1.1"
}

connection_info = {
    "username": "admin",
    "port": 22
}

router = router_info | connection_info
print(router) # {'hostname': 'R1', 'ip': '10.1.1.1', 'username': 'admin', 'port': 22}

# setdefault()
# setdefault() gets a value if the key exists.
# If the key doesn't exist, it creates the key with a default value. 
router = {
    "hostname": "R1"
}
router.setdefault("vendor", "Cisco")
print(router) # {'hostname': 'R1', 'vendor': 'Cisco'}
router.setdefault("hostname", "R2")
print(router) # {'hostname': 'R1', 'vendor': 'Cisco'}
# it doesn't replace "R1"

# from keys
# Create a dictionary from a collection of keys
interfaces = ["Gi0/0", "Gi0/1", "Gi0/2"]
status = dict.fromkeys(interfaces, "down")
print(status) # {'Gi0/0': 'down', 'Gi0/1': 'down', 'Gi0/2': 'down'}

# copy()
# Dictionaries are mutable, so assignment can create an important problem.
router1 = {
    "hostname": "R1"
}
router2 = router1
router2["hostname"] = "R2"
print(router1)

# you might expect
{"hostname": "R1"}
# but, you will get
{"hostname": "R2"}

# because
router2 = router1 # doesn't create a new dictionary. both refer to the same dictionary
router2 = router1.copy() # now they're separate dictionaries

