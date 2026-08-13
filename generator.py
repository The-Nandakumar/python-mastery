# Generator

# Generators are functions that can pause and resume their execution. 
# They are defined using the `def` keyword
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator object.

def get_device():
    yield "cisco"
    yield "juniper"
    yield "arista"

for device in get_device():
    print(device)

# The yield keyword

# The yield keyword is what makes a function a generator. 
# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, execution resumes from where it left off.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for number in count_up_to(5):
    print(number)

# Unlike return, which terminate the function, yield pauses it and can be called multiple times.

# Memory efficiency

# Generators are memory efficient because they generate values on-the-fly instead of storing in memory.

def large_sequence(n):
    for i in range(n):
        yield i

gen = large_sequence(1000000)
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Using next() with generators allows you to retrieve the next value in the sequence without iterating through the entire sequence.

def simple_gen():
    yield "Hello"
    yield "World"

gen = simple_gen()
print(next(gen))  # Output: Hello
print(next(gen))  # Output: World

# Generator expressions
# Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets.

# list comprehension
list_comp = [x * x for x in range(5)]
print(list_comp)  # Output: [0, 1, 4, 9, 16]

# generator expression
gen_exp = (x * x for x in range(5))
print(gen_exp)  # Output: <generator object <genexpr> at 0x...>
print(next(gen_exp))  # Output: 0
print(next(gen_exp))  # Output: 1
print(list(gen_exp))  # Output: [4, 9, 16] (remaining values)

# Generator methods
# Generators have built-in methods like send(), throw(), and close() that allow you to interact with the generator.

# send() method allows you to send a value to the generator, which can be used to modify its behavior.
# throw() method allows you to raise an exception inside the generator.
# close() method allows you to terminate the generator.

# example of send(), throw(), and close() methods
def echo():
    while True:
        received = yield
        print(f"Received: {received}")

gen = echo()
next(gen)  # Start the generator
gen.send("Hello")  # Output: Received: Hello
gen.send("World")  # Output: Received: World
# gen.throw(Exception("Test Exception"))  # Raises an exception inside the generator
gen.close()  # Terminates the generator

# Yield from
# Yield from allows one generator to yield values from another generator or iterable.

def cisco_devices():
    yield "R1"
    yield "R2"

def juniper_devices():
    yield "J1"
    yield "J2"

def all_devices():
    yield from cisco_devices()
    yield from juniper_devices()

for device in all_devices():
    print(device)
