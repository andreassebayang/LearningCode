# Python - Output varibles

### The print() function is used to output variables.

x = "Python is awesome"
print(x)

### In the print() funtion, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#### You can also use the + operator to output multiple variables:
x = "Python"
y = "is"
z = "awesome"
print(x + y + z) ### Notice the space character "python" and "is", without them the result would be "Pythonisawesome". To fix this, add a space character at the end of each variable, like this:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z) ### Now the result will be "Python is awesome".


# For number, the + operator works as a mathematical operator, adding the numbers:
x = 5
y = 10
print(x + y) ### The result will be 15, not 510.


### in the print() function, you can use the + operator to output multiple variables, but you cannot use the + operator to output a string and a number, like this:
# x = 5
# y = "John"
# print(x + y) ### This will result in an error, because Python does not know how to add a number and a string. You can only concatenate a string to another string. T

### The best way to output multiple variables in the print() function is to separate them with a comma, like this:
x = 5
y = "John"
print(x, y) ### This will result in "5 John", without any errors.