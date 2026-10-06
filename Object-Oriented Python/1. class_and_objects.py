# OOPs!

# OOP is programming style that is based on the concept of objects.
# "Objects" represent real-world entities.
# Every object has Attributes and Methods.

# Attributes = Variables
# Methods = Functions

# Example:
# Human is an object.
# Attributes of Human: Name, Age, Height, Weight
# Methods of Human: Walk(), Talk(), Eat(), Sleep()

# Class

# A class is a blueprint or template for creating objects.That's it.
# It defines
#   What data an object will hold (Attributes)
#   What operations can be performed on that data (Methods)
# Class is just the design of an object.

# Object

# An Object is a real, usable instance of a class.
# Class = blueprint
# Object = Actual thing created from the blueprint (class)

# You cannot use a class directly but you can use the object created from it.
# Objects = State + Behavior ( Attributes + Methods )

# Concept	    Meaning
# Class	        Blueprint/template
# Object	    Actual thing created from class
# Attributes	Data inside object
# Methods	    Functions inside class that act on object



# Real-life analogy
# Think of a Phone object:

# Attributes → battery %, brightness, model
# These values = state
# When state changes → phone behaves differently

# brightness = 100% (screen bright)
# brightness = 10% (screen dim)



# State = what the object “knows”.
# Methods = what the object “does”.

# A variable hold data but an attribute holds the data belonging to an object or class
# Variable - Free-floating data
# Attributes - data attached to something (object or class)

class Dog:
    def bark(self):
        print("Bow Bow!")

d = Dog()
d.bark()

# Output
# Bow Bow!


# Pillars of OOPs
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction