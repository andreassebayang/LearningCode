# Python Data Types

### Buil-in Data Types
### In programming, data types is an important concept. Variables can store data of different tuypes, and different types can do different thing. 



### Python has the following data types bulit-in by default, in these categories:

### ------------------------------------------------------
### Text Type      :   str
### Numeric Types  :   int, float, complex
### Boolean Type   :   bool
### Binary Types   :   bytes, bytearray, memoryview
### Sequence Types :   list, tuple, range
### Set Types      :   set, frozenset
### Non types      :   NoneType

## Getting the Data Type
"""
You can get the data type of any object by using the type() function:"""    

x = 5
print(type(x))


## Setting the Data Type
"""
Example                                         |          Data Type
===================================================================
x = "Hello World"                               |             str
x = 20                                          |             int
x = 20.5                                        |             float
x = 1j                                          |             complex  
x = ["apple", "banana", "cherry"]               |             list
x = ("apple", "banana", "cherry")               |             tuple
x = range(6)                                    |             range
x = {"name" : "John", "age" : 36}               |             dict
x = {"apple", "banana", "cherry"}               |             set
x = frozenset({"apple", "banana", "cherry"})    |             frozenset
x = true                                        |             bool
x = b"Hello"                                    |             bytes
x = bytearray(5)                                |             bytearray
x = memoryview(byte(5))                         |             memoryview
x = none                                        |             NoneType
"""


## Setting the specific Data Type
### If you want to specify the data type, you can use the following constrcutor functions:
"""
Example                                         |          Data Type
===================================================================
x = str"Hello World"                            |             str
x = int(20)                                     |             int
x = float(20.5)                                 |             float
x = complex(1j)                                 |             complex  
x = list(("apple", "banana", "cherry"))         |             list
x = tuple(("apple", "banana", "cherry"))        |             tuple
x = range(6)                                    |             range
x = dict(name="John", age=36                    |             dict
x = set(("apple", "banana", "cherry"))          |             set
x = frozenset({"apple", "banana", "cherry"})    |             frozenset
x = bool(5)                                     |             bool
x = bytes(5)                                    |             bytes
x = bytearray(5)                                |             bytearray
x = memoryview(byte(5))                         |             memoryview
x = none                                        |             NoneType
"""