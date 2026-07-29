# Constructor

# A constructor is a special method that is automatically called when an object of a class is created. 
# It is used to initialize the attributes of the class. 
# In Python, the constructor method is defined using the `__init__` method.

class Router:
    def __init__(self):
        print("Router Created")

r1 = Router()  # Output: Router Created

# Notice: We never called r1.__init__() directly. It was automatically called when we created the object r1.

# without constructor
class Router:
    pass

r1 = Router()
r1.hostname = "R1"
r1.ip_address = "10.1.1.1"
r1.vendor = "Cisco"

# Every time we create a new object, we have to manually set the attributes. This is not efficient, if the number of attributes is large.
# with constructor

class Router:
    def __init__(self, hostname, ip_address, vendor):
        self.hostname = hostname
        self.ip = ip_address
        self.vendor = vendor

r1 = Router("R1","10.1.1.1","Cisco")

# Self

# Suppose
# r1 = Router("R1")
# Python actually does something like
# Router.__init__(r1, "R1")
# so self = r1
# Inside constructor
# self.hostname = hostname means r1.hostname = "R1"
# So self always refers to the current object

# Parameters
# Constructor can receive values

class Router:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

r1 = Router("R1", "10.1.1.1")

# Attributes

# Now hostname = R1, ip = 10.1.1.1 becomes attributes
# Inside constructor we create attributes
# Attributes are simply a variable that belongs to an object

# Default values
# Default values can be assigned in parameters
# Sometimes most routers use SSH port 22 so

class Router:
    def __init__(self, hostname, port=22):
        self.hostname = hostname
        self.port = port

r1 = Router("R1")
print(r1.port, r1.hostname)
r2 = Router("R2", 830) #If another device uses different port
print(r2.port, r2.hostname)

# Optional parameter
# Sometimes API token may not exist so,

class Device:
    def __init__(self, hostname, token= None):
        self.hostname = hostname
        self.token = token
# Works
d1 = Device("R1") 
print(d1.hostname)
print(d1.token)
# This also works
d2 = Device("R2", "asd1as5d4asd2")
print(d2.hostname)
print(d2.token)

# Constructor validation
# Constructor can verify data

class Router:
    def __init__(self, ip):
        if "." not in ip:
            raise ValueError("Invalid IP")

        self.ip = ip

r1 = Router("10.1.1.1")
# r2 = Router("abcd")
print(r1.ip)
# print(r2.ip)

