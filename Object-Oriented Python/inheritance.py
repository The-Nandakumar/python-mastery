# Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Device:
    def connect(self):
        print("Connecting...")

class Cisco(Device):
    pass

router = Cisco()
router.connect()  # Output: Connecting...

# Cisco automatically gets everything from Device

# super()
# super() is a built-in function that lets a child class access methods and constructors from its parent class.
# Inheritance gives access to the parents methods. It does not automatically execute them.

# Parent
class Device:
    def __init__(self):
        print("Device Created")

# Child
class Cisco(Device):
    def __init__(self):
        print("Cisco Created")

Cisco()  # Output: Cisco Created
# python only ran Cisco's __init__

class Cisco(Device):
    def __init__(self):
        super().__init__()
        print("Cisco Created")


Cisco() # Output: Device Created \n Cisco Created

# Method Overriding
# When a child class provides a specific implementation of a method that is already defined in its parent class, it's called method overriding.

# Parent 
class Device:
    def backup(self):
        print("Generic backup")

# Child
class Cisco(Device):
    def backup(self):
        print("Cisco backup")

device = Cisco()
device.backup()  # Output: Cisco backup

# isinstance()
# Checks if an object is created from this class or its parent class. Returns True or False.

router = Cisco()
print(isinstance(router, Cisco))  # Output: True


# issubclass()
# Checks if a class is a subclass of another class. Returns True or False.
print(issubclass(Cisco, Device))  # Output: True

# Types of Inheritance
# 1. Single inheritance
# A child class inherits from a single parent class. This is called single inheritance.


# 2. Multilevel inheritance
# A child class acts as a parent class for another child class. This is called multilevel inheritance.

class Device:
    pass

class NetworkDevice(Device):
    pass

class CiscoRouter(NetworkDevice):
    pass

# 3. Hierarchical inheritance
# Many children share one parent class. This is called hierarchical inheritance.

class Device:
    pass

class Cisco(Device):
    pass

class Juniper(Device):
    pass

class Arista(Device):
    pass

# 4. Multiple inheritance
# A child class can inherit from multiple parent classes. This is called multiple inheritance.

class SSH:
    def connect(self):
        print("SSH")

class Logging:
    def log(self):
        print("Logging")

class Cisco(SSH, Logging):
    pass

c = Cisco()
c.connect()  # Output: SSH
c.log()      # Output: Logging

# Method Resolution Order (MRO)
# This one becomes important when we have multiple inheritance. 
# Python uses the C3 linearization algorithm to determine the method resolution order. 
# You can check the MRO of a class using the __mro__ attribute or the mro() method.

class SSH:
    def connect(self):
        print("SSH")

class Telnet:
    def connect(self):
        print("Telnet")

class Cisco(SSH, Telnet):
    pass

# Both SSH and Telnet have a connect method. When we call c.connect(), Python will use the MRO to determine which connect method to call.
print(Cisco.__mro__)  # Output: (<class 'Cisco'>, <class 'SSH'>, <class 'Telnet'>, <class 'object'>)
# Python searches in this order: Cisco -> SSH -> Telnet -> object.