# What is a decorator?
# A decorator is a special function that takes another function (or a class) as input, extends or modifies its behavior and returns the enhanced function.
# We reuse the decorator function

# Rules
# 1. A decorator must accept a callable as its input argument.
# 2. A decorator must return another callable (function or class) as its output.


def logging(func):

    def wrapper():
        print("Start logging...")
        func()
        print("Finished logging...")
    return wrapper

def add():
    print(10 + 20)

log = logging(add) # This log become callable function
log() # This will call the wrapper function

# Output:
# Start logging...
# 30
# Finished logging...

# Another way to use decorator is by using @ symbol before the function name
@logging
def add():
    print(10 + 20)
add()

#How to send arguments
def logging(func):

    def wrapper(*args): # args can take multiple arguments. its a tuple and it can be unpacked automatically
        # Instead of args, we can also use num1, num2 in this case
        print("Start logging...")
        func(*args) # unpacking the arguments
        print("Finished logging...")
    return wrapper

@logging
def add(num1, num2):
    print(num1 + num2)

add(20, 20)


# Where it will usefull
    # Logging
    # Caching
    # Authentication
    # Validation
    # Measuring time