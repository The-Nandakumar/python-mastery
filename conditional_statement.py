# Conditional Statements
# conditional statements are used to make decisions in a program.
# They allow your code to execute different blocks based on whether a contdition is true or false.

# 1. if statement
# The if statement executes a block of code if a specified condition is true.

# if condition:
    # block of code to be executed if the condition is true

age = 20
if age >= 18:
    print("You are eligible to vote.")

# Output: You are eligible to vote.

# 2. if-else statement
# The else block executes when the if condition is false.

age = 15
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Output: You are not eligible to vote.

# 3. if-elif-else statement
# The elif statement allows you to check multiple conditions.

age = 65
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Output: You are a senior citizen.

# 4. Nested if statements
# You can also use if statements inside another if statement.

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You are eligible to drive.")
    else:
        print("You are old enough but don't have a license.")
else:
    print("You are not old enough to drive.")

# Output: You are old enough but don't have a license.

# 5. Logical operators
# You can use logical operators to combine multiple conditions.
age = 20
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# Output: You are not eligible to drive.