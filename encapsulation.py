# Encapsulation

# Encapsulation means bundling data and methods into a single class. 
# It restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the methods and data.  

# instead of accessing the data directly, we can use getter and setter methods to access and update the data. This is called data hiding.


class Router:
    def __init__(self):
        self.hostname = "R1"

    def connect(self):
        print(f"Connecting to {self.hostname}")

router = Router()
router.connect()  # Output: Connecting to R1

# Here, hostname -> Data
# connect() -> Method

# 1. Public members
# A member is simply anything that belongs to a class. It can be a variable or a method.
# Public members are accessible from outside the class. 
# By default, all members of a class are public.

# 2. Protected members (_)
# Single underscore ( _variable )
# The underscore is only a convention meaning "Please don't access this directly". Python does not stop you.
# Useful for:
# - Authentication token
# - Session object
# - SSH connection

# 3. Private members (__)
# Double underscore ( __variable )
class Test:
    def __init__(self):
        self.__youcantaccessme = "You can't access me directly"

test = Test()
# print(test.__youcantaccessme)  # This will raise an AttributeError because the attribute is private
# Python changes the name internally to _Test__youcantaccessme, so you can still access it using that name, but it's not recommended.
# Private members helps to avoid accidental access and modification of data.
# Usefull for:
# - Passwords
# - API keys
# - Other sensitive information

# Getter method
# Used to read private attributes
class Test:
    def __init__(self):
        self.__youcantaccessme = "You can't access me directly, but you can read me using a getter method"

    def get_youcantaccessme(self):
        return self.__youcantaccessme

test = Test()
print(test.get_youcantaccessme()) # Output: You can't access me directly, but you can read me using a getter method
# so instead of test.__youcantaccessme, we use test.get_youcantaccessme() to read the private attribute.

# Setter method
# Used to modify private variables safely
class Router:
    def __init__(self):
        self.__hostname = "R1"

    def set_hostname(self, hostname):
        self.__hostname = hostname

    def get_hostname(self):
        return self.__hostname

router = Router()
router.set_hostname("NewRouter")
print(router.get_hostname())  # Output: NewRouter

# Property decorator
# Python's preferred way instead of explicit getter/setters. 

# Property getter
class Router:
    def __init__(self):
        self.__hostname = "R1"

    @property
    def hostname(self):
        return self.__hostname

router = Router()
print(router.hostname)  # Output: R1

# NOTICE: No brackets when calling the property method. This is because we are using the @property decorator, which allows us to access the method like an attribute.
# The @property decorator defines the property and its getter in one step.

# Property setter
class Router:
    def __init__(self):
        self.__hostname = "R1"

    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, value):
        self.__hostname = value

router = Router()
router.hostname = "NewRouter"
print(router.hostname)  # Output: NewRouter

# @property.setter decorator defines the setter for the property. It allows us to set the value of the property like an attribute.
