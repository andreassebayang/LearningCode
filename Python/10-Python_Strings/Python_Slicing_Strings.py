"""
Python - Slicing Strings


1.  Slicing
You can return a range of characters by using the slice syntax.
Specify the start index and the index, separated by a colon, to return a part of the sring.
"""

"""
get the character from position 2 to position 5(not included)
"""

b = "Hello, World!"
print(b[2:5])

"""
2. Slice from the Start
By leaving out the end index, the range will go to the end:
"""

"""
Get the characters from position 2, and all the way to the end
"""
b = "Hello, World!"
print(b[2:])


"""
3. Negative Indexing
Use negative indexes to start the slice from the end of the string:
"""

"""
Example:
Get the characters:
from "o" in "World" (Position -5)
To, but not included: "d" in "world! (Position -2)
"""
b = "Hello, World!"
print(b[-5:-2])