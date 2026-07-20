# Python Strings

# Strings
"""
String in python are sorrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello"

You can display a string literal with the prin() funtion
"""

print("Hello")
print('Hello')

# Quotes Inside Quotes
"""
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
"""

print("It's alright")
print("He is called 'johnny'")
print('He is called "Johnny"')

# Assign String to a Variable
"""
Assigning a string to a variable is done with the variable name allowed by an equal sign and the string:
"""

a = "Hello"
print(a)


# Multiple Strings
"""
You can assign a multiline string to a variable by using three quotes
"""

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes
a = ''' Lorem ipsum dolor sit amet
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String are Arrays
"""
Like many other popular programming languages, string in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""

"""
Get the character at position 1 (remember that the first character has the position 0)
"""
a = "Hello, World!"
print(a[1])

# Looping Through a String
"""
Since strings are arrays, we can loop throuh the characters in a string, with a for loop
"""

"""
Loop though th letters in the workd "banana"
"""
for x in "banana":
    print(x)


# String Length
"""
TO get the length of a string, use the len() function
"""
"""
The len() function returns the length of a string
"""
a = "Hello, World!"
print(len(a))

#Check String
"""
To check if a certain phrases or character is present in a string, we can use the keyworkd in
"""

"""
Chekc if "free" is present in the following text:
"""

txt = "The best things in life are free!"
print("free" in txt)


"""
Use it in an if statement
"""

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

# Check if NOT
"""
To check if a certain phrase or character is NOT present in a string, we can use the keywork not in
"""

"""
Chekc if "expensive" is NOT present in the following text:
"""

txt = "The best things in life are free!"
print("expensive" not in txt)

"""
Use it in an if statement:
"""

"""
Print only if "expensive" is not present:
"""
txt = "The best thins in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")