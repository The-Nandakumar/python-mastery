# Lambda Functions
# Lambda functions in python is a small anonymous (unnamed) function that you can define in a single line.
# It's mainly used for short, simple operations where writing a function with def would feel unnecessary.

# SYNTAX:
# lambda arguments: expression

# Simple example

add = lambda a, b: a + b
print(add(10, 20)) 

# Output: 30

# It can have any number of arguments but only one expression. The expression is evaluated and returned automatically.

# When to Use (and Not Use)
# 	Use lambda when:
# 		• The function is very short 
# 		• You need it temporarily 
# 		• It improves readability in-place 
# 	Avoid lambda when:
# 		• The logic is complex 
# 		• You need multiple steps or statements 
#       • Readability suffers