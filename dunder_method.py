# Dunder method = Double UNDERscore method. 
# They are special python methods whose names starts and ends with __ . They are also called special methods or magic methods
# Example:

__init__
__str__
__len__
__eq__
__enter__
__exit__

# The important idea is: you usually don't call dunder methods directly. Python calls them automatically when you perform certain operation.

class Router:
    def __init__(self, ip):
        self.ip = ip

# when you write:
r1 = Router("10.1.1.1")
# python effectively invokes:
Router.__init__(r1, "10.1.1.1")
# you normally just write:
Router("10.1.1.1")

# Why do dunder methods exist?
# They allow your own classes to behave like a normal python objects

class Router:
    def __init__(self, ip):
        self.ip = ip
r1 = Router("10.1.1.1")
print(r1)
# without __str__, python gives you something like
# <__main__.Router object at 0x000001...>

# You can define how your object should behave:
class Router:
    def __init__(self, ip):
        self.ip = ip
    def __str__(self):
        return f"Router({self.ip})"
# print(r1) gives Router(10.1.1.1)

# So dunder methods let you customize python's built in behavior for your objects.

# The important mental model
a + b
# for normal integer
10 + 20

# python internally uses a special method related to addition
10.__add__(20)
# similarly 
len(obj) is obj.__len__()
obj1 == obj2 is obj1.__eq__(obj2)

# So
# | What you write       | Dunder method involved       |
# | -------------------- | ---------------------------- |
# | `obj()`              | `__call__()`                 |
# | `obj + other`        | `__add__()`                  |
# | `obj == other`       | `__eq__()`                   |
# | `len(obj)`           | `__len__()`                  |
# | `str(obj)`           | `__str__()`                  |
# | `repr(obj)`          | `__repr__()`                 |
# | `obj[key]`           | `__getitem__()`              |
# | `key in obj`         | `__contains__()`             |
# | `with obj:`          | `__enter__()` / `__exit__()` |
# | `for x in obj`       | `__iter__()`                 |
# | `obj[index] = value` | `__setitem__()`              |
#  ----------------------------------------------------- 


# | Dunder method    | What it does                                                                | Example                    |
# | ---------------- | --------------------------------------------------------------------------- | -------------------------- |
# | `__init__()`     | Initializes an object when it is created. Usually used to set attributes.   | `Router("R1", "10.1.1.1")` |
# | `__str__()`      | Defines the human-readable representation of an object.                     | `print(router)`            |
# | `__repr__()`     | Defines a developer/debug-friendly representation of an object.             | `repr(router)`             |
# | `__eq__()`       | Defines how two objects are compared using `==`.                            | `router1 == router2`       |
# | `__iter__()`     | Makes an object iterable so you can use it in a `for` loop.                 | `for device in devices:`   |
# | `__getitem__()`  | Allows an object to support indexing or key-based access.                   | `devices[0]`               |
# | `__len__()`      | Defines what `len(object)` should return.                                   | `len(devices)`             |
# | `__contains__()` | Defines how the `in` operator works with your object.                       | `"R1" in devices`          |
# | `__enter__()`    | Defines what happens when entering a `with` block. Usually used for setup.  | `with connection:`         |
# | `__exit__()`     | Defines what happens when leaving a `with` block. Usually used for cleanup. | `with connection:`         |
# | `__call__()`     | Makes an object callable like a function.                                   | `connector()`              |
# | `__add__()`      | Defines how the `+` operator works between objects.                         | `interface1 + interface2`  |

class DeviceGroup:
    def __init__(self, devices):
        self.devices = devices

    def __str__(self):
        return f"DeviceGroup with {len(self.devices)} devices"

    def __repr__(self):
        return f"DeviceGroup(devices={self.devices!r})"

    def __eq__(self, other):
        return self.devices == other.devices

    def __iter__(self):
        return iter(self.devices)

    def __getitem__(self, index):
        return self.devices[index]

    def __len__(self):
        return len(self.devices)

    def __contains__(self, device):
        return device in self.devices


devices = DeviceGroup([
    "R1",
    "R2",
    "SW1"
])


# __str__()
print(devices)

# __repr__()
print(repr(devices))

# __len__()
print(len(devices))

# __getitem__()
print(devices[0])

# __contains__()
print("R1" in devices)

# __iter__()
for device in devices:
    print(device)


# __eq__()
devices2 = DeviceGroup([
    "R1",
    "R2",
    "SW1"
])

print(devices == devices2)

# Output

# DeviceGroup with 3 devices
# DeviceGroup(devices=['R1', 'R2', 'SW1'])
# 3
# R1
# True
# R1
# R2
# SW1
# True

# The main thing to understand is Dunder methods let your custom class behave like a built-in Python object