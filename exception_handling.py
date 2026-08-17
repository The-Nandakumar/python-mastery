# Exception handling in python is used to detect and handle runtime errors gracefully, preventing your program from crashing unexpectedly
# Basic syntax
try:
    # Code that may raise an exception
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")

# try, except, else and finally
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")

# try: Contains code that might cause an exception
# except: Handles specific exceptions if they occur
# else: Executes if no exception occurs
# finally: Executes regardless of whether an exception occurs or not


# Multiple exception
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
    
# Catching any exception 
try:
    x = 10 / 0

except Exception as e:
    print("An error occurred:", e)

# Raising exception
# You can raise exceptions manually using raise

age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# Custom Exception
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid age entered.")