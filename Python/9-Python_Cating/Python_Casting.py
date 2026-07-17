# Python casting
"""
Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-oriented language, and as such it uses classes to define data type, including its primitve types.

Casting in python is therefore fone using consructor functions:

1. int() - contructs an integer number from an integer literal, a float literal (by removing all decimal), or a string literal(providing the string represents a whole number)

2. float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

3. str() - construct a string from a wide variety of data types, including strings, integer literal and float literals
"""

# Integer
x = int(1)      # x will be 1
y = int(2.9)    # y will be 2
z = int("3")    # z will be 3

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# Float
x = float(1)      # x will be 1.0
y = float(2.9)    # y will be 2.9
z = float("3")    # z will be 3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


# String
x = str("s1")      # x will be 1.'s1'
y = str(2.9)    # y will be '2'
z = str("3")    # z will be '3'

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))