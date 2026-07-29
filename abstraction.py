# Abstraction
# Hiding unnecessary details and showing only what is important to the user
# Abstraction is the process of exposing only the necessary functionality while hiding the implementation details.

# Suppose you're using netmiko

from netmiko import ConnectHandler
device = ConnectHandler()

# That's it
# You don't see
# socket programming
# ↓
# SSH negotiation
# ↓
# key exchange
# ↓
# AES encryption
# ↓
# terminal initialization
# ↓
# prompt detection

# Netmiko hides all that
# This is abstraction

# Without abstraction
open_socket()
perform_ssh_handshake()
exchange_keys()
authenticate()
start_terminal()
detect_prompt()
initialize_shell()

# Instead
ConnectHandler() #Done

# Abstract Class
# A class is said to be an abstract class if it cannot be instantiated, that is you can have an object of an abstract class. 
# You can however use it as a base or parent class for constructing other classes.

# In other words,
# A parent class that cannot be used directly
# It only defines what every child must implement

# Create abstract class
# To create a abstract class in python, it must inherit the ABC class that is defined in the abc module.
# This module is available in Python's standard library.
# Moreover, the class must have at least one abstract method. Again, an abstract method is the one which cannot be called but can be overridden.
# You need to decorate it with @abstractmethod decorator.

from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

# Now Device is abstract
# When we inherit ABC, Python knows "This class is only for designing Not for creating objects"
# When we using abstractmethod it means "This method has no implementation yet but Every child MUST implement me"
# Why pass, because cisco use ssh, juniper use netconf and paloalto use api

class CiscoRouter(Device):
    def connect(self):
        print("Connected via ssh")

class JuniperRouter(Device):
    def connect(self):
        print("Connected via netconf")

# Complete Example

from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

class CiscoRouter(Device):
    def connect(self):
        print("Connected via SSH")

class JuniperRouter(Device):
    def connect(self):
        print("Connected via Netconf")

cisco = CiscoRouter()
juniper = JuniperRouter()

cisco.connect()
juniper.connect()

# Output
# Connected via SSH
# Connected via Netconf

# Different between inheritance and Abstraction
# Inheritance - Who inherits from whom?
# Abstraction - What methods must every child implements?

# Different between encapsulation and Abstraction
# Encapsulation - Focus on protecting data
# Abstraction - Focuses on hiding implementation details

# Concrete class
# A normal class that implements all inherited abstract methods and can be instantiated

# Contract
# A set of methods every child class is required to implement