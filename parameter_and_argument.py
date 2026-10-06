# Parameter
# A parameter is a variable defined in a function's definition. It acts as a placeholder for the value the function will receive.
def connect_device(ip):
    print(f"Connecting to {ip}")

# ip is a parameter

# Argument
# An argument is the actual value you pass to the function when calling it. 
connect_device("10.1.1.1")

# Multiple parameters and arguments
def connect_device(ip, username, port):
    print(ip)
    print(username)
    print(port)

connect_device("10.1.1.1", "admin", 22)

# Positional arguments
# Arguments can be matched based on their position. In the above example python maps,
# 1st argument → 1st parameter
# 2nd argument → 2nd parameter
# 3rd argument → 3rd parameter
# These are called positional arguments

# Keyword arguments
# Instead of relying on position, you can explicitly specify the parameter name. 
connect_device(ip="10.1.1.1", username = "admin", port=22)
# These are keyword arguments. The big advantage is readability.
# You can even change the order

# Default parameter
# You can give a parameter a default value
def connect_device(ip, port= 22):
    print(f"Connecting to {ip}:{port}")
connect_device("10.1.1.1")
# The above code would work
connect_device("10.1.1.1", 2222)
# Above also would work

# *args
# Sometimes we are not sure about the number of arguments the caller will provide
def show_devices(*args):
    for device in args:
        print(device)

show_devices(
    "R1",
    "R2",
    "R3"
)
# Inside the function, devices is a tuple
# Important: *args doesn't mean "arguments" specifically. args is just a conventional name.
def show_devices(*devices):
    pass
# This also works

# **kwargs
# **kwargs allows you to receive arbitrary number (An arbitrary number of keyword arguments means a function can accept any number of named inputs 
# (key=value pairs) without needing a fixed list of parameters defined in advance) of keyword arguments.
def show_device(**devices):
    print(devices)
show_device(ip="10.1.1.1", username="admin", vendor="Cisco")
# details becomes a dictionary
{
    "ip": "10.1.1.1",
    "username": "admin",
    "vendor": "Cisco"
}

# args vs kwargs
# args = Multiple positional arguments = Tuple
# kwargs = Multiple keyword arguments = Dictionary

def test(*args, **kwargs):
    print(args)
    print(kwargs)
test(10,20,30, ip="10.1.1.1", vendor="Cisco")

# Output
(10, 20, 30)

{
    "ip": "10.1.1.1",
    "vendor": "Cisco"
}

# Argument unpacking
# We can use * and ** when calling a function.
def connect(ip, username, port):
    print(ip, username, port)
device = ["10.1.1.1", "admin", 22]
connect(*device) # Equivalent to connect("10.1.1.1", "admin", 22)

def connect(ip, username, port):
    print(ip, username, port)
device = {
    "ip" : "10.1.1.1",
    "username" : "admin",
    "port" : 22
}
connect(**device) # Equivalent to connect(ip="10.1.1.1",username="admin",port=22)

# Parameter order rules
def function(required, optional=10, *args, **kwargs):
    pass