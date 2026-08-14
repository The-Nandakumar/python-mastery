# Context Manager
# A context manager is an object that controls the setup and cleanup of a resource.
# basic syntax:
# with something as something:
    # do something with something

# without context manager
file = open("example.txt", "w")
try:
    data = file.read()
finally:
    file.close()

# with context manager
with open("example.txt", "w") as file:
    data = file.read()

# it automatically takes care of closing the file after the block of code is executed, even if an exception occurs.

# Why useful?

# Production programs constantly acquire resources:
# Files
# SSH connections
# Database connections
# Network sessions
# Locks
# Temporary resources
# API sessions
# Transactions

# You don't just want to acquire these resources. You need to reliably release them.

# That's what context managers solve.

# Think of it conceptually as:
# Enter context
#      ↓
# Acquire resource
#      ↓
# Run your code
#      ↓
# Exit context
#      ↓
# Release resource

# for example, network automation:
with connect_to_router("10.1.1.1") as router:
    router.send_command("show ip interface brief")

# Conceptually,
# connect to router
#        ↓
# send commands
#        ↓
# disconnect from router

# A class can be a context manager by implementing the __enter__ and __exit__ methods.
# __enter__() is responsible for setting up/acquiring the resource.
# __exit__() handles what happens when you leave the with block.

class RouterConnection:
    def __enter__(self):
        print("Connecting to router")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnecting from router")

with RouterConnection() as router:
    print("Sending commands")

# Output:
# Connecting to router
# Sending commands
# Disconnecting from router

# Context manager decorator
from contextlib import contextmanager

@contextmanager
def router_connection():
    print("Connecting")
    try:
        yield
    finally:
        print("Disconnecting")

with router_connection():
    print("Sending commands")

# Output:
# Connecting
# Sending commands
# Disconnecting

# Execution approximately:
# 1. router_connection() is called, which prints "Connecting"
# 2. Yield statement pauses the function and returns control to the with block.
# 3. The code inside the with block is executed, printing "Sending commands"
# 4. After the with block is done, control returns to the router_connection() function, which continues after the yield statement and executes the finally block, printing "Disconnecting"

# Why try and finally?
# Because the code inside the with block can fail.

# Network automation example:
from contextlib import contextmanager

@contextmanager
def router_session(ip):
    print(f"Connecting to {ip}")

    connection = connect_to_router(ip)

    try:
        yield connection
    finally:
        print(f"Disconnecting from {ip}")
        connection.disconnect()

with router_session("10.1.1.1") as router:
    print(router.send_command("show ip interface brief"))

# We should know Class based context managers and Generator based context managers.

# Why context managers are useful?
# Context managers become valuable when the pattern repeats multiple times in your code.
# Suppose you have 20 places in your automation code:
connect()
try:
    send_command()
finally:
    disconnect()

# You're repeating the same resource-lifecycle logic everywhere.

# Without context managers

def get_router_data(ip):
    connection = connect(ip)

    try:
        return connection.send_command("show version")
    finally:
        connection.disconnect()


def get_interfaces(ip):
    connection = connect(ip)

    try:
        return connection.send_command("show ip interface brief")
    finally:
        connection.disconnect()

def get_routes(ip):
    connection = connect(ip)

    try:
        return connection.send_command("show ip route")
    finally:
        connection.disconnect()

# The actual logic is different, but the resource-lifecycle logic is the same.
# with context manager
from contextlib import contextmanager

@contextmanager
def router_connection(ip):
    connection = connect(ip)

    try:
        yield connection
    finally:
        connection.disconnect()

def get_router_data(ip):
    with router_connection(ip) as router:
        return router.send_command("show version")
def get_interfaces(ip):
    with router_connection(ip) as router:
        return router.send_command("show ip interface brief")
def get_routes(ip):
    with router_connection(ip) as router:
        return router.send_command("show ip route")