# F-String = Formatted string literal
# It lets you insert variables and expressions directly inside a string using {}.

device = "Router-01"
ip = "10.1.1.1"
print(f"Device {device} has IP {ip}")

# Output: Device Router-01 has IP 10.1.1.1

# Format specifier :
# Syntax f"{value:format_spec}
cpu = 85.6789
print(f"CPU Usage: {cpu:.2f}%")

# Output: CPU Usage: 85.68%

# Number formatting
# We can make large numbers easier to read
byte_sent = 1234567890
print(f"Byte sent:{byte_sent:,}")

# Output: Byte sent:1,234,567,890

# Width and alignment
# Useful when creating CLI-style reports
device = "Router-01"
print(f"{device:<15} ONLINE") # reserve 15 character and align value to the left

# Output: Router-01       ONLINE
print(f"{device:^15}") #Center alignment

# This becomes useful for table

print(f"{'DEVICE':<15} {'IP':<15} {'STATUS':<10}")
print(f"{'R1':<15} {'10.1.1.1':<15} {'UP':<10}")
print(f"{'R2':<15} {'10.1.1.2':<15} {'DOWN':<10}")

# Multiline f-string
# You can use f-string with multiline strings

hostname = "R1"
ip = "10.1.1.1"
status = "UP"

config = f"""
Device: {hostname}
IP: {ip}
Status: {status}
"""

print(config)

# Output:
# Device: R1
# IP: 10.1.1.1
# Status: UP