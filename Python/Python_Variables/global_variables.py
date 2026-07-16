# Python - Global Variables

#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables. global variables can be used by everyone, both inside of function and outside.

### create a variable outside of a function, and use it inside the function
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

### If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the funtion. the global variable with the same name will remain as it was, global and swith the orginal value.

### create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
    
myfunc()
print ("Python is " + x)


### The global keyword
#### Normally, when you craete a varibale inside a funtion, thata variable is local, and can only be used inside that function. To create a gloabl variable inside a fuunction, you can use the global keyword.

### If you use the globbal keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

### also, use the glaobal keyword if you want to change a global variable inside a function.
### To change the value of a gbobal variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)